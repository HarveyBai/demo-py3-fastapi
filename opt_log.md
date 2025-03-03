你是一个python开发专家，帮我在当前工作目录下创建一个venv的虚拟环境，并在此环境下初始化一个基于python3、FastApi的后端项目，遵守python3项目开发最佳实践，并且提供基于JWT的基础登录认证功能。

python -m venv venv

venv\Scripts\activate.bat

python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple

pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt] python-multipart -i https://pypi.tuna.tsinghua.edu.cn/simple

uvicorn app:app --reload --host 0.0.0.0 --port 8000
默认用户名为'johndoe'，密码为'secret'。

venv\Scripts\pip freeze > requirements.txt
venv\Scripts\pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

帮我将README.md文档补充完整，包括项目的开发规范，启动方式，测试方式，协作方式等


