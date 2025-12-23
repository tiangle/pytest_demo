class BaseConfig:
    # 用于请求设置超时时间，s
    TIME_OUT = 3


class QAConfig(BaseConfig):
    QA_SMS_URL = "https://oss-qa-ics.hanwjss.cn"
    QA_ACCOUNT = "mc123"
    QA_PASSWORD = "bb43a2c4081bec02fca7b72f38e63021"
    QA_PHONES = "17738903961"
    QA_CONTENT = "测试123数https://hi.cbmexpo.com/asdasd据测试"
    QA_SIGN = "【大汉三通】"
    QA_SUBCODE = ""
    QA_PARAMS = {"ctcTheme": "接口主题"}


# 指定当前环境
CONFIG = QAConfig
