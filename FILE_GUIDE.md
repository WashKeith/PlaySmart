# PlaySmart File Guide & Navigation

Complete reference for every file in the PlaySmart project.

---

## 📁 Directory Structure

```
PlaySmart/
├── 📄 README.md                    ⭐ START HERE - Main documentation (6000+ words)
├── 📄 QUICKSTART.md                ⭐ Get running in 5 minutes
├── 📄 SETUP_GUIDE.md               Step-by-step installation
├── 📄 INTERVIEW_GUIDE.md            Interview Q&A preparation (4000+ words)
├── 📄 PROJECT_SUMMARY.md            Complete project delivery summary
├── 📄 FILE_GUIDE.md                 This file - navigation guide
│
├── 📋 requirements.txt              Python dependencies
├── 📋 .env.example                  Environment variables template
├── 📋 .gitignore                    Git ignore rules
│
├── 📁 pipeline/                     ETL DATA PIPELINE
│   ├── 🐍 pipeline.py              ⭐ MASTER SCRIPT - Run this to fetch & transform data
│   ├── 🐍 api_config.py            API configuration & centralized parameters
│   ├── 🐍 fetch_data.py            DataFetcher class - fetch from Alpha Vantage API
│   ├── 🐍 transform.py             DataTransformer class - clean & enrich data
│   └── 🐍 __init__.py              Package initialization
│
├── 📁 dashboard/                    STREAMLIT WEB APP
│   ├── 🐍 app.py                   ⭐ MAIN DASHBOARD - Run this to see visualizations
│   ├── 📁 components/              (Future: reusable Streamlit components)
│   └── 🐍 __init__.py              Package initialization
│
├── 📁 data_raw/                     RAW DATA (Generated after running pipeline)
│   ├── stock_aapl_raw.csv
│   ├── stock_msft_raw.csv
│   ├── crypto_btc_raw.csv
│   ├── fx_usd_eur_raw.csv
│   └── ... (more asset files)
│
├── 📁 data_processed/               PROCESSED DATA (Generated after running pipeline)
│   ├── stock_aapl_processed.csv     (With metrics: MA, volatility, RSI)
│   ├── stock_msft_processed.csv
│   ├── crypto_btc_processed.csv
│   ├── fx_usd_eur_processed.csv
│   ├── pipeline_summary.txt         Execution report
│   └── ... (more asset files)
│
├── 📁 logs/                         EXECUTION LOGS (Generated after running pipeline)
│   └── pipeline_20240115_142345.log  Detailed execution log with timestamps
│
└── 📁 notebooks/                    JUPYTER NOTEBOOKS (For exploration)
    └── (Empty - add your analysis notebooks here)
```

---

## 🎯 Which File Should I Read?

### I want to...

**Get started immediately**
→ Read: [QUICKSTART.md](QUICKSTART.md) (5-minute guide)

**Install the project**
→ Read: [SETUP_GUIDE.md](SETUP_GUIDE.md) (step-by-step)

**Understand the project completely**
→ Read: [README.md](README.md) (comprehensive guide)

**Prepare for interviews**
→ Read: [INTERVIEW_GUIDE.md](INTERVIEW_GUIDE.md) (Q&A format)

**Understand the project delivery**
→ Read: [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) (what was built)

**Run the data pipeline**
→ Execute: `python pipeline/pipeline.py`

**Run the dashboard**
→ Execute: `streamlit run dashboard/app.py`

**Understand how data is fetched**
→ Read: [pipeline/api_config.py](pipeline/api_config.py) + [pipeline/fetch_data.py](pipeline/fetch_data.py)

**Understand data transformation**
→ Read: [pipeline/transform.py](pipeline/transform.py)

**Understand the full pipeline**
→ Read: [pipeline/pipeline.py](pipeline/pipeline.py)

**Understand the dashboard**
→ Read: [dashboard/app.py](dashboard/app.py)

**Deploy the project**
→ Follow instructions in [README.md](README.md) "Production Deployment" section

---

## 📚 File Descriptions

### Documentation Files

| File | Size | Purpose | Read Time |
|------|------|---------|-----------|
| **QUICKSTART.md** | 2.9 KB | 5-minute quick start guide | 5 min |
| **SETUP_GUIDE.md** | 6.8 KB | Step-by-step installation instructions | 10 min |
| **README.md** | 26.8 KB | Comprehensive project documentation | 30 min |
| **INTERVIEW_GUIDE.md** | 22.3 KB | Interview Q&A and talking points | 25 min |
| **PROJECT_SUMMARY.md** | 16.4 KB | Delivery summary and specifications | 15 min |
| **FILE_GUIDE.md** | This file | Navigation guide | 10 min |

### Configuration Files

| File | Purpose | Notes |
|------|---------|-------|
| **requirements.txt** | Python dependencies | Run `pip install -r requirements.txt` |
| **.env.example** | Environment variables template | Copy to `.env` and add API key |
| **.gitignore** | Git ignore rules | Prevents committing secrets and large files |

### Python Code

| Module | Lines | Purpose | Key Classes |
|--------|-------|---------|-------------|
| **pipeline/api_config.py** | 150 | API configuration | `APIConfig` |
| **pipeline/fetch_data.py** | 250 | Data fetching | `DataFetcher` |
| **pipeline/transform.py** | 300 | Data transformation | `DataTransformer` |
| **pipeline/pipeline.py** | 280 | Master orchestration | `DataPipeline` |
| **dashboard/app.py** | 700 | Streamlit dashboard | Page functions |

### Data Directories

| Directory | Contains | Generated By |
|-----------|----------|--------------|
| **data_raw/** | Raw CSV files from API | `pipeline.py` fetch step |
| **data_processed/** | Cleaned data with metrics | `pipeline.py` transform step |
| **logs/** | Execution logs | `pipeline.py` logging |
| **notebooks/** | Jupyter notebooks | User (for exploration) |

---

## 🚀 Typical Workflow

### Day 1: Setup & Exploration
1. Read [QUICKSTART.md](QUICKSTART.md) (5 min)
2. Follow [SETUP_GUIDE.md](SETUP_GUIDE.md) (10 min)
3. Run: `python pipeline/pipeline.py` (3 min)
4. Run: `streamlit run dashboard/app.py` (1 min)
5. Explore dashboard pages (10 min)

### Day 2: Understanding Code
1. Review comments in [pipeline/api_config.py](pipeline/api_config.py) (5 min)
2. Review comments in [pipeline/fetch_data.py](pipeline/fetch_data.py) (10 min)
3. Review comments in [pipeline/transform.py](pipeline/transform.py) (10 min)
4. Review comments in [pipeline/pipeline.py](pipeline/pipeline.py) (10 min)
5. Review dashboard structure in [dashboard/app.py](dashboard/app.py) (15 min)

### Day 3: Interview Prep
1. Read [INTERVIEW_GUIDE.md](INTERVIEW_GUIDE.md) (25 min)
2. Practice answers aloud (15 min)
3. Review [README.md](README.md) "Business Use Cases" (10 min)

---

## 🔍 Code Navigation

### To understand data fetching:
1. Start: [pipeline/api_config.py](pipeline/api_config.py) - See how API parameters are built
2. Next: [pipeline/fetch_data.py](pipeline/fetch_data.py) - See how API calls are made
3. Read: [README.md](README.md) "API Configuration" section

### To understand data transformation:
1. Start: [pipeline/transform.py](pipeline/transform.py) - See metric calculations
2. Read: [README.md](README.md) "Financial Metrics Explained" section
3. Review: Docstrings in each function (e.g., `calculate_moving_averages()`)

### To understand the full pipeline:
1. Start: [pipeline/pipeline.py](pipeline/pipeline.py) - See orchestration
2. Trace: Function calls to other modules
3. Check: Logging statements for execution flow

### To understand the dashboard:
1. Start: [dashboard/app.py](dashboard/app.py) - Lines 1-100 (imports & setup)
2. Review: Page functions (starting around line 200)
3. Understand: Chart functions (starting around line 100)

---

## 📊 Data Flow Diagram

```
┌─────────────────────────────────────────────────────┐
│        Alpha Vantage API (Real Market Data)         │
└────────────────────┬────────────────────────────────┘
                     │
                     ↓
        ┌────────────────────────────┐
        │  pipeline/fetch_data.py     │
        │  DataFetcher class          │
        │  • fetch_stock_daily()      │
        │  • fetch_crypto_daily()     │
        │  • fetch_fx_daily()         │
        └────────────┬─────────────────┘
                     │
                     ↓
        ┌────────────────────────────┐
        │   Raw Data (CSV)            │
        │   data_raw/*.csv            │
        │   • stock_aapl_raw.csv      │
        │   • crypto_btc_raw.csv      │
        └────────────┬─────────────────┘
                     │
                     ↓
        ┌────────────────────────────┐
        │ pipeline/transform.py       │
        │ DataTransformer class       │
        │ • clean_data()              │
        │ • calculate_moving_averages │
        │ • calculate_volatility()    │
        │ • calculate_rsi()           │
        └────────────┬─────────────────┘
                     │
                     ↓
        ┌────────────────────────────┐
        │ Processed Data (CSV)        │
        │ data_processed/*.csv        │
        │ • With metrics              │
        └────────────┬─────────────────┘
                     │
                     ↓
        ┌────────────────────────────┐
        │ dashboard/app.py            │
        │ Streamlit Dashboard         │
        │ • 5 Interactive Pages       │
        │ • Plotly Charts             │
        │ • Real-time Metrics         │
        └────────────┬─────────────────┘
                     │
                     ↓
        ┌────────────────────────────┐
        │  Web Browser UI             │
        │  http://localhost:8501      │
        └────────────────────────────┘
```

---

## 🎓 Learning Progression

### Beginner (Just want to use it)
1. Read: [QUICKSTART.md](QUICKSTART.md)
2. Run: `python pipeline/pipeline.py`
3. Run: `streamlit run dashboard/app.py`
4. Explore: Dashboard pages

### Intermediate (Want to understand)
1. Read: [README.md](README.md)
2. Review: Code comments in pipeline modules
3. Read: [INTERVIEW_GUIDE.md](INTERVIEW_GUIDE.md) for explanations
4. Trace: Execution flow through pipeline.py

### Advanced (Want to modify/extend)
1. Understand: Architecture in [README.md](README.md) "Architecture Overview"
2. Study: Each module in detail
3. Modify: Add more assets, new metrics, etc.
4. Deploy: Use deployment instructions in [README.md](README.md)

---

## 🔄 File Dependencies

```
.env.example
    ↓ (copy to .env, add API key)

pipeline/api_config.py
    ├─ Loads environment variables
    └─ Used by: fetch_data.py

pipeline/fetch_data.py
    ├─ Uses: api_config.py
    └─ Used by: pipeline.py

pipeline/transform.py
    └─ Used by: pipeline.py

pipeline/pipeline.py
    ├─ Uses: api_config.py, fetch_data.py, transform.py
    ├─ Reads from: .env
    ├─ Writes to: data_raw/, data_processed/, logs/
    └─ Used by: User (run manually)

dashboard/app.py
    ├─ Reads from: data_processed/
    └─ Used by: User (run with streamlit)

requirements.txt
    └─ Used by: pip install command
```

---

## ✅ Pre-Interview Checklist

Before your interview, review:

- [ ] Read [QUICKSTART.md](QUICKSTART.md) - Know the project's quick overview
- [ ] Read [INTERVIEW_GUIDE.md](INTERVIEW_GUIDE.md) - Review all Q&A
- [ ] Review [README.md](README.md) "Interview Talking Points" section
- [ ] Understand [pipeline/api_config.py](pipeline/api_config.py) - Explain API setup
- [ ] Understand [pipeline/fetch_data.py](pipeline/fetch_data.py) - Explain data fetching
- [ ] Understand [pipeline/transform.py](pipeline/transform.py) - Explain metrics
- [ ] Understand [dashboard/app.py](dashboard/app.py) - Explain dashboard architecture
- [ ] Can run the pipeline without errors
- [ ] Can explain the data flow (see diagram above)
- [ ] Can discuss business use cases from [README.md](README.md)

---

## 🎯 Quick Reference

### Run the pipeline
```bash
cd pipeline
python pipeline.py
```

### View the dashboard
```bash
streamlit run dashboard/app.py
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Check logs
```bash
tail logs/pipeline_*.log  # Latest log
```

### See what was processed
```bash
ls data_processed/
```

---

## 📝 File Modification Guide

### To add more stocks
Edit: [pipeline/pipeline.py](pipeline/pipeline.py) line ~250
Change: `stocks = ["AAPL", "MSFT", "GOOGL", "TSLA", "AMZN"]`

### To add new metrics
Edit: [pipeline/transform.py](pipeline/transform.py)
Add: New `calculate_*()` function
Call: From `transform_*_data()` functions
Update: [dashboard/app.py](dashboard/app.py) to display new metric

### To change dashboard colors
Edit: [dashboard/app.py](dashboard/app.py) line ~40 (CSS styling)

### To add new dashboard page
Edit: [dashboard/app.py](dashboard/app.py)
Add: New page function
Add: Option to sidebar navigation

---

## 🆘 File-Specific Troubleshooting

### Problem reading `.env` file
- Verify file exists: `ls -la .env`
- Check permissions: `chmod 644 .env`
- Use absolute path in code if needed

### Problem with Python imports
- Check: `__init__.py` files exist in all directories
- Add: Project root to PYTHONPATH
- Restart: Python interpreter

### Problem with data files
- Check: Directory permissions
- Verify: `data_raw/` and `data_processed/` exist
- Use: Absolute paths in configuration

---

## 📞 File Sizes & Statistics

| File | Size | Type | Lines of Code |
|------|------|------|---|
| README.md | 26.8 KB | Documentation | 500+ |
| INTERVIEW_GUIDE.md | 22.3 KB | Documentation | 400+ |
| PROJECT_SUMMARY.md | 16.4 KB | Documentation | 300+ |
| dashboard/app.py | ~20 KB | Python | 700+ |
| pipeline/pipeline.py | ~9 KB | Python | 280 |
| pipeline/transform.py | ~10 KB | Python | 300 |
| pipeline/fetch_data.py | ~9 KB | Python | 250 |
| pipeline/api_config.py | ~5 KB | Python | 150 |

**Total**: ~3,700 lines of code + 1,500+ lines of documentation

---

Made with 📊 by a data engineer passionate about making projects understandable!
