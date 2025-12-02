# PlaySmart Setup Guide

## Step-by-Step Installation

### Prerequisites
- Python 3.8 or higher
- pip (comes with Python)
- Git (optional, for version control)
- Free Alpha Vantage API key

### Step 1: Get Your API Key

1. Go to [https://www.alphavantage.co/](https://www.alphavantage.co/)
2. Click "GET FREE API KEY"
3. Enter your email and submit
4. Check your email for the API key link
5. Copy your API key (40-character string)

### Step 2: Clone or Download the Project

**Option A: Clone with Git**
```bash
git clone https://github.com/yourusername/PlaySmart.git
cd PlaySmart
```

**Option B: Download ZIP**
1. Download the repository as ZIP
2. Extract to a folder
3. Open terminal in that folder

### Step 3: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

You should see `(venv)` at the start of your terminal line.

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- pandas, numpy (data processing)
- requests (API calls)
- python-dotenv (environment variables)
- streamlit (dashboard)
- plotly (charts)
- scikit-learn, scipy (calculations)

### Step 5: Configure API Key

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your API key
# Open .env in your text editor and replace:
# ALPHA_VANTAGE_API_KEY=your_api_key_here
```

**On Windows**, you can do this in Command Prompt:
```bash
copy .env.example .env
# Then open .env in Notepad and edit
```

### Step 6: Run the Pipeline

```bash
# Navigate to pipeline directory
cd pipeline

# Run the data pipeline
python pipeline.py
```

**Expected output:**
```
2024-01-15 14:23:45 - __main__ - INFO - Starting PlaySmart Data Pipeline
2024-01-15 14:23:46 - fetch_data - INFO - Fetching game deal data...
2024-01-15 14:23:47 - fetch_data - INFO - Successfully fetched deal records
...
2024-01-15 14:25:30 - __main__ - INFO - PlaySmart Data Pipeline Completed Successfully!
```

**This creates:**
- `data_raw/` – Raw CSV files from API
- `data_processed/` – Cleaned data with metrics
- `logs/` – Execution logs

### Step 7: Run the Dashboard

From the project root:

```bash
streamlit run dashboard/app.py
```

**Expected output:**
```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
```

The dashboard opens automatically. If not, visit `http://localhost:8501` in your browser.

### Step 8: Explore the Dashboard

Navigate the 5 pages:
1. **Market Overview** – Global snapshot
2. **Stocks** – AAPL, MSFT, GOOGL, TSLA, AMZN analysis
3. **Crypto** – BTC, ETH analysis
4. **FX** – USD/EUR, USD/JPY analysis
5. **Insights** – Market analytics and forecasts

---

## ✅ Verification Checklist

After setup, verify everything works:

- [ ] Python 3.8+ installed (`python --version`)
- [ ] Virtual environment activated (see `(venv)` in terminal)
- [ ] Dependencies installed (`pip list` shows pandas, streamlit, etc.)
- [ ] `.env` file created with API key
- [ ] Pipeline ran without errors
- [ ] `data_processed/` folder has CSV files
- [ ] Dashboard starts and loads data
- [ ] All 5 dashboard pages work

---

## 🐛 Troubleshooting

### Problem: "ALPHA_VANTAGE_API_KEY not set"

**Solution**:
1. Check `.env` file exists in project root (not in pipeline folder)
2. Check `.env` contains: `ALPHA_VANTAGE_API_KEY=your_actual_key`
3. Restart terminal and reactivate virtual environment

### Problem: "ModuleNotFoundError: No module named 'streamlit'"

**Solution**:
1. Activate virtual environment (see Step 3)
2. Run: `pip install -r requirements.txt`
3. Verify: `pip list` shows streamlit

### Problem: "Connection timeout" or "Rate limit exceeded"

**Solution**:
1. Free tier allows 5 requests/minute
2. Pipeline has built-in delays (0.5s between requests)
3. If still rate-limited, wait 1 minute and retry
4. Or get premium API key from Alpha Vantage

### Problem: "No CSV files in data_processed/"

**Solution**:
1. Check pipeline logs: `tail logs/pipeline_*.log`
2. Verify API key is valid by testing:
   ```bash
   cd pipeline
   python -c "from api_config import APIConfig; print(APIConfig.API_KEY)"
   ```
3. Check network connection
4. Try running pipeline again

### Problem: "Dashboard shows 'No data available'"

**Solution**:
1. Ensure pipeline ran successfully (check logs)
2. Ensure CSV files exist in `data_processed/`
3. Restart Streamlit: press `Ctrl+C` and re-run `streamlit run dashboard/app.py`
4. Clear cache: delete `~/.streamlit/` or use Streamlit's cache clear option

### Problem: "Port 8501 already in use"

**Solution**:
```bash
# Run on different port
streamlit run dashboard/app.py --server.port 8502
```

---

## 📊 Running on Different Schedules

### One-time run:
```bash
cd pipeline
python pipeline.py
```

### Hourly updates (requires Airflow):
```bash
pip install apache-airflow
# Create DAG configuration
```

### Daily automated (Windows Scheduled Task):
1. Create batch file `run_pipeline.bat`:
   ```
   @echo off
   cd C:\path\to\PlaySmart\pipeline
   python pipeline.py
   ```
2. Open Task Scheduler
3. Create Basic Task → Set schedule to Daily → Point to `run_pipeline.bat`

---

## 🚀 Next Steps

After successful setup:

1. **Explore the code**
   - Read comments in `pipeline/pipeline.py`
   - Review metric calculations in `pipeline/transform.py`
   - Study dashboard pages in `dashboard/app.py`

2. **Customize**
   - Add more stocks: Edit `pipeline.py` line with `stocks = [...]`
   - Change dashboard colors: Modify CSS in `dashboard/app.py`
   - Add new metrics: Implement in `transform.py` and integrate into dashboard

3. **Deploy**
   - **Streamlit Cloud**: Connect GitHub repo, auto-deploy from main branch
   - **Heroku**: Dockerfile provided, push to Heroku
   - **Docker**: Build image, run containers

4. **Learn**
   - Check README.md for deep-dive documentation
   - Review INTERVIEW_GUIDE.md for technical concepts
   - Explore notebooks/ for experimental analysis

---

## 📞 Support

If you hit issues:

1. **Check logs**:
   ```bash
   tail -f logs/pipeline_*.log
   ```

2. **Test components individually**:
   ```bash
   cd pipeline
   python -c "from fetch_data import DataFetcher; fetcher = DataFetcher(); df = fetcher.fetch_stock_daily('AAPL'); print(f'Got {len(df)} records')"
   ```

3. **Review error messages** – They're detailed and point to the issue

4. **Check Alpha Vantage API docs**: https://www.alphavantage.co/documentation/

---

## ✨ You're Ready!

Once everything works:
- ✅ You have a production-ready data pipeline
- ✅ You have a professional analytics dashboard
- ✅ You can talk about this in interviews with confidence
- ✅ You can customize it for different use cases

Happy analyzing! 📊
