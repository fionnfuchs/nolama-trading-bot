# Nolama Trading Bot
Nolama is a simple, extendable trading bot. It is able to trade live with the Alpaca API. It can easily be extended and backtested. I have also tested it with historical bitcoin data. An example for Bitcoin can be found as a Jupyter Notebook in the repo and on Colab below.

WARNING: This bot can not make consistent profit as is.

## Run

### Colab (recommended)

You can run the bot using this notebook in colab:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fionnfuchs/nolama-trading-bot/blob/master/jupyter/nolama_notebook.ipynb) 

See how it works with Bitcoin:
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/fionnfuchs/nolama-trading-bot/blob/master/jupyter/nolama_bitcoin_notebook.ipynb) 


### With Docker

1. Clone the repository

2. Build and run

```
docker build -t nolama:bot .

docker run -it nolama:bot
``` 

### Virtual Environment (without Docker)

1. Clone the repository 
2. Create and activate virtual environment 

```
python3 -m venv env

source env/bin/activate
``` 

3. Install dependencies 

```
pip install -r "requirements.txt"
``` 

4. Run

```
python3 nolama/run.py
``` 

## Performance 
Currently tested on three timeframes of $AAPL (each roughly 3 days) with minute ticks. The bot trades profitable for these three timeframes even if the overall price trend is negative. The bot underperforms the stock for the timeframe where the price trend is very positive. 

Example plot of bot trading $AAPL (bot bought stock at green circles and sold at red circles): 

![Example Plot](/img/example_plot.png)

## Extend 
You can extend the bot by implementing TA Calculation Steps and Scoring Steps and adding them to the bot. You will need to set the `score_threshold` value accordingly. 
