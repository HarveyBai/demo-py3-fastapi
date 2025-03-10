import signal
import sys
import uvicorn
from app.boot import create_app
from app.config import settings

app = create_app()

def signal_handler(sig, frame):
    """处理终止信号，确保应用程序优雅退出"""
    print("\n正在关闭应用程序...")
    sys.exit(0)

if __name__ == "__main__":
    # 注册信号处理器
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug
    )