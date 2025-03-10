from contextlib import asynccontextmanager
from fastapi import FastAPI
from .logger import app_logger
from .database import engine


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用程序生命周期管理

    负责在应用启动时初始化各个组件，在关闭时清理资源。

    Args:
        app: FastAPI应用实例
    """
    # 初始化日志系统
    app_logger.info("应用程序启动中...")
    app_logger.debug("正在初始化系统组件")

    # 初始化数据库连接
    conn = await engine.connect()
    # 检查数据库中是否存在users表
    result = await conn.run_sync(lambda sync_conn: sync_conn.dialect.has_table(sync_conn, 'users'))

    # 初始化缓存服务
    # await cache_service.init()

    try:
        yield
    finally:
        # 关闭数据库连接
        if conn:
            await conn.close()  # 使用close()方法来释放连接
        # 关闭缓存服务
        # await cache_service.close()


def create_app() -> FastAPI:
    """创建FastAPI应用实例

    初始化FastAPI应用，配置生命周期管理，注册路由等。

    Returns:
        FastAPI: 配置完成的FastAPI应用实例
    """
    app = FastAPI(
        title="FastAPI Demo",
        description="A demo FastAPI project with JWT authentication",
        version="0.1.0",
        lifespan=lifespan
    )

    # 配置CORS
    from fastapi.middleware.cors import CORSMiddleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # 导入路由
    from .routes import auth, ollama

    # 注册路由
    app.include_router(auth.router)
    app.include_router(ollama.router)

    return app
