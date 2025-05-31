import matplotlib.pyplot as plt
import os
import logging

def generate_plot(df, ticker='AAPL'):
    try:
        os.makedirs('reports', exist_ok=True)
        logging.info(" Generating plot...")
        plt.figure(figsize=(12, 6))
        plt.plot(df.index, df['Close'], label='Close Price', linewidth=2)
        plt.plot(df.index, df['MA20'], label='MA20', linestyle='--')
        plt.title(f'{ticker} Price & Moving Average')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        output_path = f'reports/{ticker}_chart.png'
        plt.savefig(output_path)
        plt.close()
        logging.info(f" Plot saved to {output_path}")
        return output_path
    except Exception as e:
        logging.error(f" Error generating plot: {e}")
        return None

def generate_html_report(df, ticker='AAPL'):
    try:
        last_change = ((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100
        avg_volatility = df['Volatility'].mean()

        html_content = f"""
        <html>
            <head><title>Report for {ticker}</title></head>
            <body>
                <h1>Report for {ticker}</h1>
                <p>Last 30 days change: {last_change:.2f}%</p>
                <p>Average volatility: {avg_volatility:.2f}</p>
                <img src="{ticker}_chart.png" alt="Price Chart">
            </body>
        </html>
        """
        report_path = f'reports/{ticker}_report.html'
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(html_content)
        logging.info(f" HTML report saved to {report_path}")
        return report_path
    except Exception as e:
        logging.error(f" Error generating HTML report: {e}")
        return None

if __name__ == "__main__":
    import logging
    from logging_setup import setup_logging
    from process_data import process_data

    setup_logging()
    df = process_data()
    if df is not None:
        plot_path = generate_plot(df)
        report_path = generate_html_report(df)

