from typing import Final
import pandas as pd
import concurrent.futures
from gradio_client import Client, handle_file

_url: Final = "http://localhost:7860"
_user: Final = "admin"
_password: Final = "admin"
_model_name: Final = "hosted_vllm/Qwen/Qwen2.5-VL-7B-Instruct-AWQ"


def dataframe_to_custom_dict(df: pd.DataFrame) -> dict:
    return {
        "headers": df.columns.tolist(),
        "data": df.values.tolist(),
        "metadata": None,  # 如果需要元数据请修改
    }


def dict_to_dataframe(d: dict) -> pd.DataFrame:
    return pd.DataFrame(d["data"], columns=d["headers"])


def get_extracted_fields_and_tables(
    client_url: str,
    username: str,
    password: str,
    model_name: str,
    fields_and_tables: dict,
    file_inputs: list[dict],
):
    client = Client(client_url, auth=(username, password))
    result = client.predict(
        file_inputs=file_inputs,
        model_name=model_name,
        fields_and_tables=fields_and_tables,
        api_name="/extract_information",
    )
    fields_results, tables_results = result
    fields_df = dict_to_dataframe(fields_results)
    tables_df = dict_to_dataframe(tables_results)
    return fields_df, tables_df


fields_and_tables = dataframe_to_custom_dict(
    pd.DataFrame(
        [
            {
                "name": "invoice_number",
                "type": "field",
                "description": "Invoice number",
            },
            {
                "name": "item_description",
                "type": "table",
                "description": "Item/Product description",
            },
            # 根据需要添加更多字段和表格列
        ]
    )
)

file_inputs = [
    {
        # "image": handle_file("https://your_image_url/invoice.jpg") # 如果图片托管在互联网上
        "image": handle_file("assets/invoice_test.jpeg")  # 如果图片存储在本地机器上
    }
]

## 发送单个请求
### 客户端URL可以是本地主机或公共URL，如 `https://6986bdd23daef6f7eb.gradio.live/`
fields_df, tables_df = get_extracted_fields_and_tables(
    _url,
    _user,
    _password,
    _model_name,
    fields_and_tables,
    file_inputs,
)
print("========Fields:=========")
print(fields_df)
print("========Tables:=========")
print(tables_df)


## 并行发送多个请求
# 定义用于并行执行的包装函数
def run_request():
    return get_extracted_fields_and_tables(
        _url,
        _user,
        _password,
        _model_name,
        fields_and_tables,
        file_inputs,
    )


# 使用ThreadPoolExecutor并行发送10个请求
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    future_results = [executor.submit(run_request) for _ in range(10)]

    for future in concurrent.futures.as_completed(future_results):
        fields_df, tables_df = future.result()
        print("========Fields:=========")
        print(fields_df)
        print("========Tables:=========")
        print(tables_df)
