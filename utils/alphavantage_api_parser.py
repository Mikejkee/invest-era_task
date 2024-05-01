import os

import requests


def get_top_alphavantage_gainers_losers(api_key, num_top_gainers=10, num_top_losers=10):
    """
    Get the top gainers and losers from the Alpha Vantage API.

    :param api_key: Alpha Vantage API key
    :param num_top_gainers:
    :param num_top_losers:
    :return: list of top gainers and losers
    """

    url = f'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    top_gainers = data['top_gainers']
    top_losers = data['top_losers']

    top_10_gainers = top_gainers[:num_top_gainers]
    top_10_losers = top_losers[:num_top_losers]

    return top_10_gainers, top_10_losers
