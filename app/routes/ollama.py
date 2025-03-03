from fastapi import APIRouter, Depends, HTTPException, Body
from typing import Dict, Any, Optional
from ..services.ollama_service import OllamaService
from ..models.ollama import GenerateRequest, GenerateResponse, ModelsResponse

router = APIRouter(prefix="/api/ollama", tags=["ollama"])

# 创建OllamaService实例
ollama_service = OllamaService()

@router.post("/generate", response_model=GenerateResponse, description="生成AI文本", summary="生成AI文本")
async def generate_text(request: GenerateRequest = Body(..., description="生成文本的请求参数")) -> GenerateResponse:
    """生成文本

    Args:
        model (str): 模型名称
        prompt (str): 输入提示
        system (Optional[str], optional): 系统提示. Defaults to None.
        temperature (float, optional): 采样温度. Defaults to 0.7.

    Returns:
        GenerateResponse: 包含生成文本、模型信息和性能指标的响应
    """
    try:
        response = await ollama_service.generate(
            model=request.model,
            prompt=request.prompt,
            system=request.system,
            temperature=request.temperature
        )
        return GenerateResponse(**response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/models", response_model=ModelsResponse)
async def list_models() -> ModelsResponse:
    """获取可用模型列表

    Returns:
        ModelsResponse: 包含可用模型列表的响应
    """
    try:
        response = await ollama_service.list_models()
        return ModelsResponse(**response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.on_event("shutdown")
async def shutdown_event():
    """应用关闭时清理资源"""
    await ollama_service.close()