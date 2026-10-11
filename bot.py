import yfinance as yf
import requests
from datetime import datetime

TOKEN = "8930031913:AAGAFxEmI5LMrDCDa5w1XbN8xLQeP0o7r7sT6vU"
CHAT_ID = "8628332432"

HALAL = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "NVDA", "META", "ADBE", "AVGO", "ORCL"]

def send(msg):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    try:
        r = requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=10)
        print(r.text)
    except Exception as e:
        print(f"Error sending: {e}")

found = False
now = datetime.now().strftime("%H:%M")
log_msg = ""

for ticker in HALAL:
    try:
        data = yf.download(ticker, period="2d", interval="1d", progress=False, auto_adjust=True)
        if len(data) < 2:
            continue
        prev_close = float(data['Close'].iloc[-2])
        open_price = float(data['Open'].iloc[-1])
        gap = ((open_price - prev_close) / prev_close) * 100
        if abs(gap) >= 2.5:
            send(f"🚀 فجوة حلال! {ticker} الفجوة: {gap:.2f}% السعر: ${open_price:.2f}")
            found = True
    except Exception as e:
        print(f"{ticker} error: {e}")
        continue

if not found:
    send(f"✅ تم الفحص الساعة {now} - لا يوجد فجوات حاليا\nيراقب {len(HALAL)} أسهم حلال")
else:
    send(f"✅ الفحص اكتمل الساعة {now}")
