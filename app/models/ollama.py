from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List

class GenerateRequest(BaseModel):
    """文本生成请求模型"""
    model: str = Field(
        ...,
        description="要使用的AI模型名称，例如：llama2、codellama等",
        example="llama2"
    )
    prompt: str = Field(
        ...,
        description="需要AI模型回答的问题或完成的任务描述",
        example="请解释什么是人工智能？"
    )
    system: Optional[str] = Field(
        None,
        description="用于设定AI助手的角色和行为规范的系统提示词",
        example="你是一个专业的AI助手，请用通俗易懂的语言回答问题"
    )
    temperature: float = Field(
        0.7,
        description="控制AI回答的随机性和创造性的温度参数，值越高回答越多样化，值越低回答越确定性",
        ge=0.0,
        le=1.0,
        example=0.7
    )

class GenerateResponse(BaseModel):
    """文本生成响应模型"""
    model: str = Field(
        ...,
        description="生成此回答的AI模型名称",
        example="llama2"
    )
    response: str = Field(
        ...,
        description="AI模型生成的回答内容",
        example="人工智能是指通过计算机程序模拟人类智能的技术..."
    )
    created_at: str = Field(
        ...,
        description="响应生成的时间戳",
        example="2024-01-20T10:30:15.123Z"
    )
    done: bool = Field(
        ...,
        description="标识是否已完成全部文本生成",
        example=True
    )
    context: Optional[List[int]] = Field(
        None,
        description="用于保持对话连续性的上下文标记列表",
        example=[1, 2, 3, 4]
    )
    total_duration: Optional[int] = Field(
        None,
        description="生成此回答的总耗时（纳秒）",
        example=1500000000
    )
    load_duration: Optional[int] = Field(
        None,
        description="加载AI模型所需的时间（纳秒）",
        example=500000000
    )
    prompt_eval_duration: Optional[int] = Field(
        None,
        description="评估和处理输入提示词所需的时间（纳秒）",
        example=100000000
    )

class ModelInfo(BaseModel):
    """模型信息"""
    name: str = Field(..., description="模型名称")
    modified_at: str = Field(..., description="最后修改时间")
    size: int = Field(..., description="模型大小（字节）")
    digest: str = Field(..., description="模型摘要")

class ModelsResponse(BaseModel):
    """模型列表响应"""
    models: List[ModelInfo] = Field(..., description="可用模型列表")