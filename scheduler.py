import schedule
import time
import logging
from logging_setup import setup_logging
from fetch_data import fetch_data
from process_data import process_data
from generate_report import generate_plot, generate_html_report
import json
from ml_predict import predict_price_movement


def job():
    logging.info("Starting the automated job...")

    with open('config.json') as f:
        config = json.load(f)

    ticker = config.get('ticker', 'AAPL')
    period = config.get('period', '1mo')
    interval = config.get('interval', '1d')

    data = fetch_data(ticker, period, interval)
    if data is None:
        logging.warning("Skipping job because no data fetched.")
        return

    df = process_data(f'data/{ticker}_data.csv')
    if df is None:
        logging.warning("Skipping job because data processing failed.")
        return

    generate_plot(df, ticker)
    generate_html_report(df, ticker)

    prediction = predict_price_movement(df)
    if prediction == 1:
        logging.info(f"{ticker} prediction: UP tomorrow")
    else:
        logging.info(f"{ticker} prediction: DOWN tomorrow")

    logging.info("Automated job completed successfully.")

