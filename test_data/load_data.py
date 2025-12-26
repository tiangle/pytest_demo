import json
from pathlib import Path


class LoadJsonData:
    def __init__(self):
        pass

    @staticmethod
    def load_sms_test_data():
        # 获取项目根目录
        project_path = Path(__file__).parent.parent
        # 数据源文件路径
        json_data_path = project_path / "test_data" / "sms_test_data.json"
        with open(json_data_path, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)["sms_submit_case"]
            print(f"加载{len(data)}条case数据")
            return data

    @staticmethod
    def long_sms_content(data):
        long_content_data = []

        for item in data:
            itme_copy = item.copy()
            if item["case_name"] == "正向用例-短信内容499字":
                itme_copy["params"]["content"] = "【大汉三通】" + "字" * 493
            elif item["case_name"] == "异常用例-短信内容501字":
                itme_copy["params"]["content"] = "【大汉三通】" + "字" * 495
            elif item["case_name"] == "正向用例-短信内容500字":
                itme_copy["params"]["content"] = "【大汉三通】" + "字" * 494
            long_content_data.append(itme_copy)

        return long_content_data

    @staticmethod
    def load_dfrc_test_data():

        project_path = Path(__file__).parent.parent
        # 数据源文件路径
        json_data_path = project_path / "test_data" / "dfrc_test_data.json"
        with open(json_data_path, "r", encoding="utf-8") as json_data:
            data = json.load(json_data)["dfrc_test_data"]
            long_content_data = LoadJsonData.long_sms_content(data)
            print(f"加载{len(long_content_data)}条case数据")
            return long_content_data