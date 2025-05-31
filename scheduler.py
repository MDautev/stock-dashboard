import schedule
import time
import logging
from logging_setup import setup_logging
from fetch_data import fetch_data
from process_data import process_data
from generate_report import generate_plot, generate_html_report
import json

with open('config.json') as f:
    config = json.load(f)

ticker = config.get('ticker', 'AAPL')
period = config.get('period', '1mo')
interval = config.get('interval', '1d')


setup_logging()

def job():
    logging.info(" Starting the automated job...")
    ticker = 'AAPL'

    data = fetch_data(ticker, period, interval)
    if data is None:
        logging.warning(" Skipping job because no data was fetched.")
        return

    df = process_data(f'data/{ticker}_data.csv')
    if df is None:
        logging.warning(" Skipping job because data processing failed.")
        return

    if generate_plot(df, ticker) is None:
        logging.warning(" Skipping report generation because plot failed.")
        return

    if generate_html_report(df, ticker) is None:
        logging.warning(" Report generation failed.")
        return

    logging.info(" Automated job completed successfully.")

# Schedule the job to run every day at 10:00 AM
schedule.every(1).minutes.do(job)

logging.info(" Waiting for scheduled jobs...")
while True:
    schedule.run_pending()
    time.sleep(60)  # check every minute
