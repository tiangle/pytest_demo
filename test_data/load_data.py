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
