import os

import pandas as pd
import matplotlib.pyplot as plt

from utils.alphavantage_api_parser import get_top_alphavantage_gainers_losers
from utils.finam_parser import get_top_finam_gainers_losers


def combine_and_visualize_data(api_key, top_flag=True):
    """
    Combines the data from get_top_gainers_losers and get_top_gainers_losers,
    and visualizes it in a line chart using the matplotlib library.

    Args:
        top_flag (bool, optional): Whether to get the top gainers or losers. Defaults to True.

    """
    top_index = 0 if top_flag else 1

    top_gainers_losers_1 = get_top_alphavantage_gainers_losers(api_key)
    top_gainers_losers_1 = [data for data in top_gainers_losers_1[top_index]
                            if 'ticker' in data and 'change_percentage' in data]
    top_gainers_losers_2 = get_top_finam_gainers_losers()[top_index]

    combined_data = top_gainers_losers_2 + top_gainers_losers_1

    df = pd.DataFrame(combined_data)

    # Строим гистограмму
    plt.figure(figsize=(10, 6))
    plt.bar(df['ticker'], df['change_percentage'])
    plt.xlabel('ticker')
    plt.ylabel('Change Percentage (%)')
    plt.title('Stock Change Percentage by Ticker')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.show()


if __name__ == '__main__':
    api_key = os.environ.get('API_KEY')
    combine_and_visualize_data(api_key, top_flag=False)
