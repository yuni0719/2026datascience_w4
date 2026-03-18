import yfinance as yf
import requests
import os
import random

def send_telegram_msg(message):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    requests.post(url, data=payload)

def get_random_stock():
    # 隨機挑選幾個熱門標的
    stocks = ["2330.TW", "2317.TW", "2454.TW", "0050.TW", "AAPL", "TSLA"]
    target = random.choice(stocks)
    
    stock = yf.Ticker(target)
    data = stock.history(period="1d")
    latest_price = round(data['Close'].iloc[-1], 2)
    return target, latest_price

if __name__ == "__main__":
    try:
        symbol, price = get_random_stock()
        msg = f"🤖 自動回報：\n標的：{symbol}\n當前股價：{price}"
        send_telegram_msg(msg)
    except Exception as e:
        send_telegram_msg(f"❌ 執行出錯了：{e}")
