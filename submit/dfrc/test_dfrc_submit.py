import pytest
from unittest.mock import patch

from api.SmaApi import SmaApi
from config.config import DFRC_CONFIG
from exceptions.exceptions import ApiRequestError
from test_data.load_data import LoadJsonData
from util.md5_util import md5_util


@pytest.fixture(scope="module")
def dfrc_fixture():
    dfrc_url = f"{DFRC_CONFIG.DFRC_SMS_URL}/xxxx"
    dfrc_body = {
        "userName": DFRC_CONFIG.DFRC_USERNAME,
        "password": DFRC_CONFIG.DFRC_PASSWORD,
        "mobile": DFRC_CONFIG.DFRC_MOBILE,
        "content": DFRC_CONFIG.DFRC_CONTENT,
        "dstime": DFRC_CONFIG.DFRC_DSTIME,
        "seqid": DFRC_CONFIG.DFRC_SEQID,
        "isms": DFRC_CONFIG.DFRC_ISMS,
    }
    return {"dfrc_url": dfrc_url, "dfrc_body": dfrc_body}


@pytest.mark.parametrize("case_data", LoadJsonData.load_dfrc_test_data())
def test_dfrc_submit(dfrc_fixture, case_data):
    try:
        temp_body = dfrc_fixture["dfrc_body"].copy()
        sign = md5_util.md5_encode(
            temp_body["userName"] + temp_body["password"] + temp_body["mobile"] + temp_body["content"])
        temp_body.update({"sign": sign})

        # 合并用例参数
        case_data_copy = case_data.copy()
        # 判断是否有sign参数，有且不为空，从params中移除
        if case_data_copy["params"].get("sign") is not None:
            case_data_copy["params"].pop("sign")
        body = {**temp_body, **case_data_copy["params"]}

        # 发送请求并断言
        response = SmaApi().dfrc_submit(dfrc_fixture["dfrc_url"], body)
        assert response["resultCode"] == case_data["expected"][
            "resultCode"], f"接口响应码为{response['resultCode']}，响应描述为{response['resultMsg']}，与预期响应码 {case_data['expected']['resultCode']} ，响应描述{case_data['expected']['resultMsg']}，不一致"
    except ApiRequestError as e:
        pytest.fail(f"用例[{case_data['case_name']}]失败：接口请求失败，请检查地址配置或网络连接", pytrace=False)
    except AssertionError as e:
        print(f"用例[{case_data['case_name']}]失败")
        raise
    except Exception as e:
        pytest.fail(f"用例[{case_data['case_name']}]执行失败")
