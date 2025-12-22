# 接口自动化框架学习(自用）
基于 Python + pytest + requests 实现的短信接口自动化测试框架  
python版本Python 3.13.9  
需要安装pytest、requests


## config.py
集中管理所有通用、静态、可复用的配置信息

## sms_test_data.json
测试数据，集中存储所有测试场景的输入结果与预期结果
具体业务代码中可以使用@pytest.mark.parametrize实现数据驱动  
case中“内容为空”的是测试断言失败，需要成功将result更改为21即可
