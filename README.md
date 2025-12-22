接口自动化框架学习流程


config.py
集中管理所有通用、静态、可复用的配置信息

sms_test_data.json
测试数据，集中存储所有测试场景的输入结果与预期结果
具体业务代码中可以使用@pytest.mark.parametrize实现数据驱动
