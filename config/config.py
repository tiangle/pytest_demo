class BaseConfig:
    SMS_URL = "https://oss-qa-ics.hanwj.cn"
    # 用于请求设置超时时间，s
    TIME_OUT = 3


class QAConfig(BaseConfig):
    QA_SMS_URL = BaseConfig.SMS_URL
    QA_ACCOUNT = "mc123"
    QA_PASSWORD = "bb43a2c4081bec02fca7b72f38e63021"
    QA_PHONES = "17712345678"
    QA_CONTENT = "测试123数https://hi.cbmexpo.com/asdasd据测试"
    QA_SIGN = "【大汉三通】"
    QA_SUBCODE = ""
    QA_PARAMS = {"ctcTheme": "接口主题"}

class DFRCConfig(BaseConfig):
    DFRC_SMS_URL = BaseConfig.SMS_URL
    DFRC_USERNAME = "mc123"
    DFRC_PASSWORD = "bb43a2c4081bec02fca7b72f38e63021"
    DFRC_SIGN = ""
    DFRC_DSTIME = ""
    DFRC_MOBILE = "17712345678"
    DFRC_CONTENT = "【大汉三通】发送内容测试"
    DFRC_SEQID = ""
    DFRC_ISMS = 0

# 指定当前环境
CONFIG = QAConfig
DFRC_CONFIG = DFRCConfig