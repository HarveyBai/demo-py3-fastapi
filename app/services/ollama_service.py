from typing import Optional, Dict, Any
import httpx
from ..config import get_settings
from ..logger import app_logger

# 获取配置实例
settings = get_settings()

class OllamaService:
    def __init__(self):
        """初始化Ollama服务，从环境配置中读取基础URL"""
        settings = get_settings()
        self.base_url = settings.ollama_base_url.rstrip('/')
        self.client = httpx.AsyncClient(timeout=settings.ollama_timeout)

    async def generate(self, 
                      model: str, 
                      prompt: str, 
                      system: Optional[str] = None,
                      temperature: float = 0.7,
                      **kwargs) -> Dict[str, Any]:
        """生成文本响应

        Args:
            model (str): 要使用的模型名称
            prompt (str): 输入提示
            system (Optional[str]): 系统提示
            temperature (float): 采样温度

        Returns:
            Dict[str, Any]: 生成的响应
        """
        payload = {
            "model": model,
            "prompt": prompt,
            "temperature": temperature,
            **kwargs
        }
        if system:
            payload["system"] = system

        try:
            app_logger.debug(f"Generating text with model {model}, prompt length: {len(prompt)}")
            response = await self.client.post(f"{self.base_url}/api/generate", json=payload)
            response.raise_for_status()
            result = await response.json()
            app_logger.debug(f"Successfully generated text with model {model}")
            return result
        except Exception as e:
            app_logger.error(f"Error generating text with model {model}: {str(e)}")
            raise

    async def list_models(self) -> Dict[str, Any]:
        """获取可用模型列表

        Returns:
            Dict[str, Any]: 模型列表
        """
        try:
            app_logger.debug("Fetching available models")
            async with self.client.get(f"{self.base_url}/api/tags") as response:
                response.raise_for_status()
                result = response.json()
                app_logger.debug(f"Successfully fetched {len(result.get('models', []))} models")
                return result
        except Exception as e:
            app_logger.error(f"Error fetching models list: {str(e)}")
            raise

    async def close(self):
        """关闭HTTP客户端"""
        await self.client.aclose()