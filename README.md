# demo-py3-fastapi

## API接口

### Ollama服务接口

- `POST /api/ollama/generate`: 生成AI文本
  - 请求参数：
    - `model`: 模型名称（必填）
    - `prompt`: 输入提示（必填）
    - `system`: 系统提示（可选）
    - `temperature`: 采样温度（可选，默认0.7，范围0.0-1.0）
  - 响应参数：
    - `model`: 使用的模型名称
    - `response`: 生成的文本响应
    - `created_at`: 响应创建时间
    - `done`: 是否完成生成
    - `context`: 上下文标记（可选）
    - `total_duration`: 总耗时（纳秒）
    - `load_duration`: 模型加载耗时（纳秒）
    - `prompt_eval_duration`: 提示词评估耗时（纳秒）

- `GET /api/ollama/models`: 获取可用模型列表
  - 响应参数：
    - `models`: 可用模型列表
      - `name`: 模型名称
      - `modified_at`: 最后修改时间
      - `size`: 模型大小（字节）
      - `digest`: 模型摘要
