# 操作日志记录

```sh
.venv\Scripts\activate  # 激活虚拟环境
deactivate  # 退出虚拟环境

pytest --cov=.  # 查看测试覆盖率报告
pytest --cov=. --cov-report=term-missing  # 查看测试覆盖率报告（显示未覆盖的代码）
pytest --cov=. --cov-report=html  # 查看测试覆盖率报告（生成html报告）
pytest --cov=. --cov-report=term-missing --cov-report=html  # 查看测试覆盖率报告（显示未覆盖的代码，生成html报告）

uv add pytest pytest-cov python-dotenv loguru httpx  # 安装基础组件库
uv add fastapi uvicorn[standard] debugpy # 安装fastapi
uv add sqlalchemy  # 安装sqlalchemy
uv add ruff  # 安装ruff   

uv run .\src\demo_py3_fastapi\main.py  # 运行fastapi
uvicorn src.demo_py3_fastapi.main:app --host 0.0.0.0 --port 8000 --reload # 运行fastapi
```

