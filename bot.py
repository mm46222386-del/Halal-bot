import urllib.request, json, ssl
ssl._create_default_https_context = ssl._create_unverified_context
TOKEN="8930031913:AAGAFxEml5LMrDCDa5w1RQpUn5zs2wxgALg"
CHAT_ID="1887062091"
def send(t):
 try:
  d=json.dumps({"chat_id":CHAT_ID,"text":t}).encode()
  r=urllib.request.Request(f"https://api.telegram.org/bot{TOKEN}/sendMessage",data=d,headers={"Content-Type":"application/json"})
  urllib.request.urlopen(r,timeout=10)
 except: pass
def gap(s):
 try:
  url=f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?interval=5m&range=1d"
  req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
  with urllib.request.urlopen(req,timeout=10) as rr:
   c=[x for x in json.loads(rr.read())['chart']['result'][0]['indicators']['quote'][0]['close'] if x]
   if len(c)>=2:
    return (c[-1]-c[-2])/c[-2]*100,c[-1]
 except: pass
 return 0,0
HALAL=["AAPL","MSFT","NVDA","GOOGL","META","AMD","AVGO","COST","ADBE","QCOM"]
for s in HALAL:
 g,p=gap(s)
 if g>=2.5:
  send(f"🚀 {s} فجوة حلال +{g:.2f}% - ${p:.2f}")
