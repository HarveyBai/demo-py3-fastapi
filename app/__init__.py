from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="FastAPI Demo",
    description="A demo FastAPI project with JWT authentication",
    version="0.1.0"
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 导入路由
from app.routes import auth, ollama

# 注册路由
app.include_router(auth.router)
app.include_router(ollama.router)