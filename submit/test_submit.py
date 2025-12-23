from pathlib import Path

import pytest
import requests
import json
from config import CONFIG


# 自定义接口异常
class ApiRequestError(Exception):
    pass


def load_sms_test_data():
    # 使用当前文件所在目录的父目录作为数据源目录
    json_path = Path(__file__).parent
    # 数据源文件路径
    json_data_path = json_path.parent / "test_data" / "sms_test_data.json"
    with open(json_data_path, "r", encoding="utf-8") as json_data:
        data = json.load(json_data)["sms_submit_case"]
        print(f"加载{len(data)}条case数据")
        return data


def submit(url, body):
    try:
        response = requests.post(url, json=body, timeout=CONFIG.TIME_OUT)
        response.raise_for_status()
        response_test = json.loads(response.text)
        response_result = int(response_test["result"])
        response_desc = response_test["desc"]
        return {"result": response_result, "desc": response_desc}
    except Exception as e:
        raise ApiRequestError from e


class TestSubmit:
    @pytest.fixture(scope='module')
    def sms_fixture(self):
        url = CONFIG.QA_SMS_URL + "/json/sms/Submit"
        account = CONFIG.QA_ACCOUNT
        password = CONFIG.QA_PASSWORD
        content = CONFIG.QA_CONTENT
        phones = CONFIG.QA_PHONES
        sign = CONFIG.QA_SIGN
        subcode = CONFIG.QA_SUBCODE
        params = CONFIG.QA_PARAMS
        body = {"account": account,
                "password": password,
                "phones": phones,
                "content": content,
                "sign": sign,
                "subcode": subcode,
                "params": params}
        return {"url": url, "body": body}

    # 数据驱动
    @pytest.mark.parametrize("case_data", load_sms_test_data())
    def test_post_submit_case(self, sms_fixture, case_data):
        try:
            # 合并数据源
            body = {**sms_fixture.get("body"), **case_data["params"]}
            response = submit(sms_fixture.get("url"), body)

            assert response["result"] == case_data["result"], \
                f"用例[{case_data['case_name']}]失败：预期 result={case_data['result']}，实际={response['result']}"
            assert response["desc"] == case_data["desc"], \
                f"用例[{case_data['case_name']}]失败：预期 desc={case_data['desc']}，实际={response['desc']}"
            print(f"用例[{case_data['case_name']}]成功")
        except ApiRequestError as e:
            # 自定义异常内容，关闭堆栈信息打印
            pytest.fail("接口异常或超时，请检查配置或网络环境", pytrace=False)
        except AssertionError as e:
            print(f"用例[{case_data['case_name']}]失败")
            raise
        except Exception as e:
            raise
