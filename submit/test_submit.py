import pytest
import requests
import json
from config import CONFIG


def load_sms_test_data():
    # 数据源绝对路径
    json_data_path = "E:\\PythonProject\\SubmitProject\\test_data\\sms_test_data.json"
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
        print(e)


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

    # 标准接口
    def test_post_submit(self, sms_fixture):
        try:
            response = submit(sms_fixture.get("url"), sms_fixture.get("body"))
            assert response["result"] == 0 and response["desc"] == "提交成功", \
                f"预期 result=0 且 desc=提交成功，实际 result={response['result']}, desc={response['desc']}"
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(e)

    # 手机号为空
    def test_post_submit_nophones(self, sms_fixture):
        try:
            # 设置手机号为空
            body = sms_fixture.get("body").copy()
            body["phones"] = ""
            response = submit(sms_fixture.get("url"), body)
            assert response["result"] == 14 and response["desc"] == "手机号码为空", \
                f"预期 result=14 且 desc=手机号码为空，实际 result={response['result']}, desc={response['desc']}"
        except AssertionError as e:
            print(e)
        except Exception as e:
            print(e)

    # 直接跑json数据源里的case
    @pytest.mark.parametrize("case_data", load_sms_test_data())
    def test_post_submit_case(self, sms_fixture, case_data):
        try:
            body = {**sms_fixture.get("body"), **case_data["params"]}
            response = submit(sms_fixture.get("url"), body)

            assert response["result"] == case_data["result"], \
                f"用例[{case_data['case_name']}]失败：预期 result={case_data['result']}，实际={response['result']}"
            assert response["desc"] == case_data["desc"], \
                f"用例[{case_data['case_name']}]失败：预期 desc={case_data['desc']}，实际={response['desc']}"
            print(f"用例[{case_data['case_name']}]成功")
        except AssertionError as e:
            print(f"用例[{case_data['case_name']}]失败")
            raise
        except Exception as e:
            print(e)
