from fastapi.testclient import TestClient

# 确保正确导入您的 FastAPI app 实例
# 假设您的 app 实例在 src/demo_py3_fastapi/main.py 文件中名为 'app'
from demo_py3_fastapi.main import app

# 同样，如果您的 AppConfig 在测试时需要被正确加载，请确保相关配置已设置
# from demo_py3_fastapi.config.my_config import AppConfig # AppConfig 会在导入 app 时被间接加载

# 使用您的 FastAPI app 初始化 TestClient
client = TestClient(app)


def test_read_main_root():
    """
    测试 FastAPI 应用程序的根端点 ("/")。
    """
    response = client.get("/")
    assert response.status_code == 200
    # 根据您根端点的实际响应调整期望的 JSON
    # 基于您之前 main.py 中 root 函数的定义，它会返回包含 AppConfig 信息的字典
    # 假设 AppConfig 使用的是默认值
    # expected_json = {
    #     "message": "Hello World",
    #     "app_name": "RuoYi-FasAPI",  # 这是 AppSettings 中的默认值
    #     "app_version": "1.0.0",     # 这是 AppSettings 中的默认值
    #     "app_env": "dev"            # 这是 AppSettings 中的默认值
    # }
    expected_json = {"message": "Hello World"}
    assert response.json() == expected_json


# 您可以删除或重构之前尝试使用 'main()' 函数的旧测试:
# def test_main_output(): ...
# def test_main_with_mock(): ...
# def test_main_parametrize(expected_output): ...
# def test_main_entry_point(): ...

# 如果您有其他端点，可以添加更多类似 test_read_main_root 的测试函数。
# 例如，如果您有一个端点 /items/{item_id}:
# def test_read_item():
#     response = client.get("/items/foo") # 假设不需要 header
#     assert response.status_code == 200
#     assert response.json() == {
#         "id": "foo",
#         "title": "Foo",
#         "description": "Some description",
#     }
