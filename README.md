# Nolama Trading Bot
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fionnfuchs/nolama-trading-bot/blob/master/trading_bot.ipynb)
Nolama is a simple, extendable trading bot. It is able to trade live with the Alpaca API. It can easily be extended and backtested. Currently implemented in a Jupyter notebook. 

WARNING: This bot can not make consistent profit as is.

## Run
Just run the notebook. Insert your Alpaca API Key and Secret in the cell at the top. If you do not have an Alpaca account you will need to provide your own closing price lists for backtesting and live trading will not work as is. 

## Performance 
Currently tested on three timeframes of $AAPL (each roughly 3 days) with minute ticks. The bot trades profitable for these three timeframes even if the overall price trend is negative. The bot underperforms the stock for the timeframe where the price trend is very positive. 

## Extend 
You can extend the bot by implementing TA Calculation Steps and Scoring Steps and adding them to the bot. You will need to set the `score_threshold` value accordingly. 
