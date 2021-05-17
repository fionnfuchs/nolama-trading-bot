# Nolama Trading Bot
Nolama is a simple, extendable trading bot. It is able to trade live with the Alpaca API. It can easily be extended and backtested. 

WARNING: This bot can not make consistent profit as is.

## Run

You can run the bot using this notebook in colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fionnfuchs/nolama-trading-bot/blob/master/jupyter/nolama_notebook.ipynb) 

Alternatively clone the repository, install the dependencies using pip and run `nolama/run.py`.

## Performance 
Currently tested on three timeframes of $AAPL (each roughly 3 days) with minute ticks. The bot trades profitable for these three timeframes even if the overall price trend is negative. The bot underperforms the stock for the timeframe where the price trend is very positive. 

Example plot of bot trading $AAPL (bot bought stock at green circles and sold at red circles): 

![Example Plot](/img/example_plot.png)

## Extend 
You can extend the bot by implementing TA Calculation Steps and Scoring Steps and adding them to the bot. You will need to set the `score_threshold` value accordingly. 
