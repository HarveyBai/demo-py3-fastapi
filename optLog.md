# 操作日志记录

```sh
.venv\Scripts\activate  # 激活虚拟环境
deactivate  # 退出虚拟环境
uv pip install --upgrade pip  # 升级pip

uv sync --extra dev  # 同步开发环境, 包含dev依赖
uv pip install -e .  # 安装项目为可编辑模式

pytest --cov=.  # 查看测试覆盖率报告
pytest --cov=. --cov-report=term-missing  # 查看测试覆盖率报告（显示未覆盖的代码）
pytest --cov=. --cov-report=html  # 查看测试覆盖率报告（生成html报告）
pytest --cov=. --cov-report=term-missing --cov-report=html  # 查看测试覆盖率报告（显示未覆盖的代码，生成html报告）

uv add pytest pytest-cov ruff debugpy -G dev  # 安装开发依赖
uv add python-dotenv loguru httpx  # 安装基础组件库
uv add fastapi uvicorn[standard] # 安装fastapi
uv add sqlalchemy  # 安装sqlalchemy

# 设置pythonpath
set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project\root
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/root"  
# 安装项目为可编辑模式,链接`src`目录到虚拟环境的`site-packages`中，使Python解释器能够找到项目中的模块。
uv pip install -e ".[dev]"  # 安装项目为可编辑模式（包含开发依赖）

uv run .\src\demo_py3_fastapi\main.py  # 运行fastapi
uv add pydantic_settings
uvicorn src.demo_py3_fastapi.main:app --host 0.0.0.0 --port 8000 --reload # 运行fastapi
```

