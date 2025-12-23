# 短信接口自动化测试框架
自用学习项目

基于 Python + pytest + requests 实现的短信接口自动化测试框架，用于全面测试短信发送功能的各种场景。

## 项目特点

- ✅ **数据驱动**：测试用例与测试数据分离，支持JSON格式数据文件
- ✅ **参数化测试**：使用pytest参数化特性，一套代码测试多种场景
- ✅ **灵活配置**：支持多环境配置管理，便于切换测试环境
- ✅ **统一响应处理**：封装接口请求和响应解析逻辑，提高代码复用性
- ✅ **完整异常处理**：对接口请求异常和断言失败进行不同处理
- ✅ **清晰的测试报告**：结合pytest-html生成直观的测试报告
- ✅ **跨平台兼容**：使用相对路径和动态路径处理，支持不同操作系统

## 技术栈

- **Python**: 3.13.9
- **pytest**: 测试框架
- **requests**: HTTP请求库
- **pytest-html**: 生成HTML测试报告
- **json**: 数据格式处理

## 项目结构

```
SubmitProject/
├── submit/
│   ├── __pycache__/         # Python编译缓存
│   └── test_submit.py       # 测试用例代码
├── test_data/
│   └── sms_test_data.json   # 测试数据文件
├── __pycache__/             # Python编译缓存
├── .idea/                   # IDE配置文件
├── README.md                # 项目说明文档
└── config.py                # 配置文件
```

## 安装与依赖

### 依赖安装
```bash
# 安装pytest
pip install pytest

# 安装requests
pip install requests

# 安装pytest-html (可选，用于生成HTML测试报告)
pip install pytest-html
```

## 配置文件 (config.py)

集中管理所有通用、静态、可复用的配置信息，支持多环境配置：

```python
class BaseConfig:
    # 用于请求设置超时时间，s
    TIME_OUT = 3


class QAConfig(BaseConfig):
    QA_SMS_URL = "https://oss-qa-ics.hanwj.cn"
    QA_ACCOUNT = "mc123"
    QA_PASSWORD = "bb43a2c4081bec02fca7b72f38e63021"
    QA_PHONES = "17738903961"
    QA_CONTENT = "测试123数https://hi.cbmexpo.com/asdasd据测试"
    QA_SIGN = "【大汉三通】"
    QA_SUBCODE = ""
    QA_PARAMS = {"ctcTheme": "接口主题"}


# 指定当前环境
CONFIG = QAConfig
```

## 测试数据 (sms_test_data.json)

集中存储所有测试场景的输入和预期结果，支持多种测试场景：

### 数据格式
```json
{
  "sms_submit_case": [
    {
      "case_name": "测试用例名称",
      "params": {
        "phones": "接收手机号码",
        "content": "短信内容",
        "sign": "短信签名",
        "其他参数": "参数值"
      },
      "result": 预期结果代码,
      "desc": "预期结果描述"
    }
  ]
}
```

### 支持的测试场景
- 正向用例：正常短信发送
- 多个手机号码发送
- 国际号码格式
- 自定义msgid
- 自定义subcode
- 自定义params
- ctcTheme短信主题统计
- urlReplace长链接替换
- 各种异常场景测试

## 测试用例 (test_submit.py)

### 核心功能

1. **测试数据加载**：从JSON文件加载测试数据
2. **接口请求封装**：统一的HTTP请求处理函数
3. **测试用例设计**：
   - 基础功能测试
   - 异常场景测试
   - 数据驱动测试

### 自定义异常
```python
class ApiRequestError(Exception):
    """自定义接口请求异常"""
    pass
```

## 运行测试

### 直接运行pytest (推荐)
```bash
# 在项目根目录下运行所有测试
python -m pytest submit/test_submit.py -v

# 生成HTML测试报告
python -m pytest submit/test_submit.py -v --html=report.html
```

### 直接运行测试脚本
```bash
# 直接运行测试脚本
python submit/test_submit.py
```

## 测试结果说明

### 响应参数
- **result**: 提交结果代码
- **desc**: 状态描述
- **msgid**: 短信编号
- **failPhones**: 错误号码列表
- **taskid**: 长链接替换任务编号

### 常见错误码
- `0`: 提交成功
- `1`: 账号或密码错误
- `3`: msgid太长，不得超过64位
- `4`: 错误号码/限制运营商号码
- `8`: 定时时间格式错误
- `14`: 手机号码为空
- `21`: 短信内容为空
- `24`: 无可用号码


## 注意事项

1. 测试数据中的账号密码为测试环境配置，请勿用于生产环境
2. 定时发送功能需要确保时间格式正确
3. 国际号码发送需要开通国际功能
4. 长链接替换功能需要确保链接格式符合要求
5. 使用回调地址功能需要提前配置账号


自用学习项目