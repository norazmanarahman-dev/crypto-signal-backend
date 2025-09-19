# Crypto Signal Backend

A simple backend service to fetch cryptocurrency candle data from Binance API.

## Features
- Fetch historical candle data
- Built with FastAPI
- Easy to extend for trading strategies

## Installation

```bash
git clone https://github.com/norazmanarahman-dev/crypto-signal-backend.git
cd crypto-signal-backend
pip install -r requirements.txt
```

## Usage

Run the backend:
```bash
uvicorn main:app --reload
```

Then open in browser:
```
http://127.0.0.1:8000/candles/BTCUSDT?interval=1h&limit=10
```

