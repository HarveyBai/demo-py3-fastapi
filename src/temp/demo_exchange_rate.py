import httpx
import json
from datetime import datetime

# ====================== 配置部分 (请根据你的需求修改) ======================

# 1. 在这里粘贴你从 ExchangeRate-API.com 获取的 API Key
API_KEY = "79b7896a7dd270823604a5cf"

# 2. 设置你关心的货币
#    基础货币 (你持有的货币)
BASE_CURRENCY = "USD"
#    目标货币 (你想要兑换的货币)
TARGET_CURRENCY = "CNY"

# 3. 设置你的买入标准
#    例如，当 1 美元可以兑换的人民币低于 7.20 时，就满足条件
#    这是一个 "小于等于" 的判断
BUY_IN_STANDARD = 7.20

# =========================================================================


def get_and_check_rate():
    """
    获取最新汇率并检查是否满足买入标准。
    """
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{BASE_CURRENCY}"

    print(
        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 开始执行任务 (使用 httpx)..."
    )

    try:
        # 修改点 2: 使用 httpx.get() 发送网络请求
        response = httpx.get(url, timeout=10.0)  # 建议设置超时时间

        # raise_for_status() 的功能和 requests 中完全相同
        response.raise_for_status()

        # json() 方法的功能也完全相同
        data = response.json()

        if data.get("result") == "success":
            rates = data.get("conversion_rates")

            if TARGET_CURRENCY not in rates:
                print(f"错误：在返回的数据中找不到目标货币 '{TARGET_CURRENCY}'。")
                return

            current_rate = rates[TARGET_CURRENCY]

            print(f"成功获取汇率：1 {BASE_CURRENCY} = {current_rate} {TARGET_CURRENCY}")
            print(
                f"你的买入标准是：1 {BASE_CURRENCY} <= {BUY_IN_STANDARD} {TARGET_CURRENCY}"
            )

            if current_rate <= BUY_IN_STANDARD:
                print(
                    f"✅ 提醒！当前汇率 ({current_rate}) 已满足你的买入标准 ({BUY_IN_STANDARD})！"
                )
            else:
                print(
                    f"❌ 未满足买入标准。当前汇率 ({current_rate}) 高于你的标准 ({BUY_IN_STANDARD})。"
                )

        else:
            error_type = data.get("error-type", "未知错误")
            print(f"API 请求失败，错误类型：{error_type}")

    # 修改点 3: 捕获 httpx 的特定异常
    except httpx.HTTPStatusError as e:
        # 这个异常对应 response.raise_for_status() 失败的情况 (如 404, 500 错误)
        print(f"HTTP 错误发生：{e.response.status_code} - {e.request.url}")
    except httpx.RequestError as e:
        # 这个异常捕获更广泛的网络/连接问题 (如 DNS 错误, 超时)
        print(f"网络请求失败：{e}")
    except json.JSONDecodeError:
        print("无法解析服务器返回的数据。")
    except Exception as e:
        print(f"发生未知错误：{e}")


# --- 主程序入口 ---
if __name__ == "__main__":

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 程序启动")
    # get_and_check_rate()
