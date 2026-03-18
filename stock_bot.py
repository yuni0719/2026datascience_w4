import yfinance as yf
import requests
import os

def send_telegram_msg(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    print(f"正在發送訊息到 ID: {chat_id}...") # 這行會出現在 GitHub 日誌裡
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    resp = requests.post(url, data=payload)
    print(f"發送狀態: {resp.status_code}, 回傳內容: {resp.text}")

if __name__ == "__main__":
    print("程式啟動中...")
    try:
        stock_id = "2330.TW"
        stock = yf.Ticker(stock_id)
        data = stock.history(period="1d")
        price = round(data['Close'].iloc[-1], 2)
        
        msg = f"📈 測試回報：{stock_id} 股價為 {price}"
        send_telegram_msg(msg)
        print("所有步驟執行完畢！")
    except Exception as e:
        print(f"發生錯誤了: {e}")
