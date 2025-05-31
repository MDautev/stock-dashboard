````markdown
# 📊 Financial Dashboard Automation

This project automates downloading, processing, and reporting of financial stock data using Python.

---

## ✨ Features

✅ Fetch financial data from Yahoo Finance (via `yfinance`)  
✅ Clean and process data (with Pandas)  
✅ Calculate indicators (moving average, volatility)  
✅ Generate plots (using Matplotlib)  
✅ Create automated HTML reports  
✅ Run as a daily automated job (via `schedule`)  
✅ Fully configurable via `config.json`

---

## 📦 Requirements

- Python 3.10+
- Libraries (see `requirements.txt`):
  - pandas
  - yfinance
  - matplotlib
  - schedule

---

## ⚙ How to Use

1️⃣ Clone this repository:

```bash
git clone <your-repo-url>
cd financial-dashboard
```
````

````

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
````

3️⃣ Edit config.json to choose your stock ticker, period, and interval:

```json
{
  "ticker": "AAPL",
  "available_tickers": ["AAPL", "MSFT", "TSLA", "GOOGL"],
  "period": "1mo",
  "interval": "1d"
}
```

4️⃣ Run the automated scheduler:

```bash
python scheduler.py
```

📁 Output
Data CSV files → saved in /data
Plots and HTML reports → saved in /reports

💡 Example
After running, check:

reports/AAPL_report.html

reports/AAPL_chart.png

You can open the HTML file in your browser to view the latest report.

🏆 Author
Made by MDautev
