# FinSight Quick Start (5 minutes)

## 🚀 TL;DR - Get Running in 5 Steps

### 1. Get API Key (2 minutes)
- Go to https://www.alphavantage.co/
- Sign up, copy your API key

### 2. Clone & Setup (1 minute)
```bash
# Navigate to your projects folder
cd C:\Users\YourUsername\FinSight

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows

# Install packages
pip install -r requirements.txt
```

### 3. Configure (1 minute)
```bash
# Copy example file
copy .env.example .env

# Edit .env (open in Notepad)
# Add your API key:
# ALPHA_VANTAGE_API_KEY=your_key_here
```

### 4. Fetch Data (2-3 minutes)
```bash
cd pipeline
python pipeline.py
```

Wait for completion message:
```
FinSight Data Pipeline Completed Successfully!
```

### 5. View Dashboard (1 minute)
```bash
# From project root
streamlit run dashboard/app.py
```

Opens at `http://localhost:8501` automatically.

---

## ✨ What You Get

✅ **5 Interactive Dashboard Pages**
- Market Overview – Global snapshot
- Stocks – Deep analysis (AAPL, MSFT, GOOGL, TSLA, AMZN)
- Crypto – BTC, ETH analysis
- FX – USD/EUR, USD/JPY, EUR/GBP rates
- Insights – Volatility, performance, forecasts

✅ **Professional Data Pipeline**
- Fetches real market data via API
- Cleans and validates
- Calculates financial metrics (MA, RSI, volatility)
- Saves processed data

✅ **Interview Ready**
- Production-quality code
- Full documentation
- Interview talking points included

---

## 📍 Key Files

| File | What It Does |
|------|-------------|
| `pipeline/pipeline.py` | Fetch data + calculate metrics (run this) |
| `dashboard/app.py` | Interactive dashboard (run this) |
| `README.md` | Full documentation (6000+ words) |
| `INTERVIEW_GUIDE.md` | Q&A for interviews (4000+ words) |

---

## ❌ Stuck?

**"ALPHA_VANTAGE_API_KEY not set"**
- Check `.env` exists in project root (not pipeline folder)
- Verify API key is copied correctly
- Restart terminal

**"ModuleNotFoundError"**
- Make sure virtual environment is activated (see `(venv)` in terminal)
- Re-run `pip install -r requirements.txt`

**"Rate limit exceeded"**
- Free tier allows 5 requests/minute
- Wait 1 minute and try again
- Pipeline has built-in delays to prevent this

**"No data in dashboard"**
- Ensure pipeline completed successfully
- Check `data_processed/` folder has CSV files
- Restart Streamlit

---

## 🎯 What's Next?

- **Learn code**: Read comments in `pipeline/api_config.py`
- **Customize**: Add more stocks by editing `pipeline.py`
- **Deploy**: Use Streamlit Cloud (free) to share dashboard
- **Interview prep**: Study `INTERVIEW_GUIDE.md`

---

## 📞 Full Documentation

- **Setup details**: See `SETUP_GUIDE.md`
- **Technical deep-dive**: See `README.md`
- **Interview talking points**: See `INTERVIEW_GUIDE.md`
- **Code walkthrough**: See inline comments in pipeline modules

---

**You're now running a professional finance analytics platform! 📊🚀**
