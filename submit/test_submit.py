from pathlib import Path

import pytest
from config.config import CONFIG
from api.SmaApi import SmaApi
from exceptions.exceptions import ApiRequestError
from test_data.load_data import LoadJsonData


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
    @pytest.mark.parametrize("case_data", LoadJsonData.load_sms_test_data())
    def test_post_submit_case(self, sms_fixture, case_data):
        try:
            # 合并数据源
            body = {**sms_fixture.get("body"), **case_data["params"]}
            response = SmaApi().submit(sms_fixture.get("url"), body)
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
