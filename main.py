from fastapi import FastAPI
import requests

app = FastAPI()

BINANCE_API = "https://api.binance.com/api/v3/klines"

@app.get("/")
def home():
    return {"message": "Crypto Signal Backend is running"}

@app.get("/candles/{symbol}")
def get_candles(symbol: str, interval: str = "1h", limit: int = 50):
    """
    Fetch candle data from Binance
    Example: /candles/BTCUSDT?interval=1h&limit=10
    """
    url = f"{BINANCE_API}?symbol={symbol}&interval={interval}&limit={limit}"
    response = requests.get(url)
    data = response.json()
    return {"symbol": symbol, "interval": interval, "candles": data}
