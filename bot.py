import yfinance as yf
import requests
import os
from datetime import datetime

TOKEN = "8930031913:AAGAFxEml5LMrDCDa5w1RQpUn5zs2wxgALg"
    CHAT_ID = "8628332432"

HALAL = ["AAPL","MSFT","GOOGL","AMZN","TSLA","NVDA","META","NFLX","ADBE","AVGO"]

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

found = False
now = datetime.now().strftime("%H:%M")
for ticker in HALAL:
    try:
        data = yf.download(ticker, period="2d", interval="1d", progress=False)
        if len(data) < 2: continue
        prev_close = float(data['Close'].iloc[-2])
        open_price = float(data['Open'].iloc[-1])
        gap = ((open_price - prev_close) / prev_close) * 100
        if abs(gap) >= 2.5:
            send(f"🚀 فجوة حلال! سهم: {ticker} فجوة: {gap:.2f}% سعر: ${open_price:.2f}")
            found = True
    except:
        continue

if not found:
    send(f"✅ تم الفحص الساعة {now} - لا يوجد فجوات حاليا\nيراقب 10 أسهم حلال")
else:
    send(f"✅ الفحص اكتمل الساعة {now}")
