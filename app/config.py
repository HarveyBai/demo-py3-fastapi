import os
from functools import lru_cache
from typing import Dict, Any

from dotenv import load_dotenv

# 确定当前环境
ENV = os.getenv("ENV", "development")

# 加载对应环境的配置文件
def load_env_file():
    # 加载环境特定的配置文件
    env_file = f".env.{ENV}"
    if os.path.exists(env_file):
        load_dotenv(env_file)
    else:
        raise FileNotFoundError(f"Configuration file {env_file} not found")

# 加载配置文件
load_env_file()

class Settings:
    # 应用配置
    app_name: str = os.getenv("APP_NAME", "FastAPI Demo")
    app_version: str = os.getenv("APP_VERSION", "1.0.0")
    debug: bool = os.getenv("DEBUG", "false").lower() == "true"
    
    # 服务器配置
    host: str = os.getenv("HOST", "0.0.0.0")
    port: int = int(os.getenv("PORT", "8000"))
    
    # 数据库配置
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    # JWT配置
    jwt_secret_key: str = os.getenv("JWT_SECRET_KEY", "your-secret-key")
    jwt_algorithm: str = os.getenv("JWT_ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # API配置
    api_prefix: str = os.getenv("API_PREFIX", "/api/v1")
    docs_url: str = os.getenv("DOCS_URL", "/docs")
    redoc_url: str = os.getenv("REDOC_URL", "/redoc")
    
    # Redis配置
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    cache_prefix: str = os.getenv("CACHE_PREFIX", "fastapi_demo")
    
    # Ollama服务配置
    ollama_base_url: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    ollama_timeout: float = float(os.getenv("OLLAMA_TIMEOUT", "30.0"))
    
    def dict(self) -> Dict[str, Any]:
        """将配置转换为字典格式

        Returns:
            Dict[str, Any]: 配置字典
        """
        return {
            "app_name": self.app_name,
            "app_version": self.app_version,
            "debug": self.debug,
            "host": self.host,
            "port": self.port,
            "database_url": self.database_url,
            "api_prefix": self.api_prefix,
            "docs_url": self.docs_url,
            "redoc_url": self.redoc_url,
            "ollama_base_url": self.ollama_base_url,
            "ollama_timeout": self.ollama_timeout,
            "redis_url": self.redis_url,
            "cache_prefix": self.cache_prefix
        }

@lru_cache()
def get_settings() -> Settings:
    """获取配置单例实例"""
    return Settings()

# 导出配置实例
settings = get_settings()