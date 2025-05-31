import yfinance as yf
import os
import logging

def fetch_data(ticker='AAPL', period='1mo', interval='1d'):
    """
    Fetch historical data for a given ticker.
    :param ticker: Stock symbol (e.g., 'AAPL')
    :param period: Time period ('1mo', '3mo', '1y', '5d', etc.)
    :param interval: Data interval ('1d', '1h', '1wk', etc.)
    :return: DataFrame with the data or None if failed
    """
    try:
        os.makedirs('data', exist_ok=True)
        logging.info(f"Fetching data for {ticker} (Period: {period}, Interval: {interval})...")
        data = yf.download(ticker, period=period, interval=interval)
        
        if data.empty:
            logging.warning(f"No data found for {ticker}.")
            return None

        output_path = f"data/{ticker}_data.csv"
        data.to_csv(output_path)
        logging.info(f"Data saved to {output_path}")
        return data

    except Exception as e:
        logging.error(f"Error fetching data for {ticker}: {e}")
        return None

if __name__ == "__main__":
    import logging
    from logging_setup import setup_logging

    setup_logging()
    fetch_data('AAPL', '1mo', '1d')
