import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import nest_asyncio
import asyncio

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.patches import Ellipse

from steps import BollingerBandsCalculation, BollingerBandsScoring
from bot import Bot

ALPACA_KEY = "PKQCV2R91BAY1D0X94HG"
ALPACA_SECRET = "vhPlO3UL35eSTUMwSDDofSJYctlZINco4dmnfQqP"

nest_asyncio.apply()

api = tradeapi.REST(ALPACA_KEY, ALPACA_SECRET, base_url='https://paper-api.alpaca.markets')
account = api.get_account()

# Configure the bot with a stock label and add calculation and scoring steps
bot = Bot("AAPL", api)
bot.calculation_steps.append(BollingerBandsCalculation(window=30, window_dev=2))
bot.scoring_steps.append(BollingerBandsScoring())

# A timeframe when $AAPL price fell
falling_aapl = api.get_bars("AAPL", TimeFrame.Minute, "2021-01-26", "2021-02-26", limit=5000, adjustment='raw').df
# A timeframe when $AAPL price rose
rising_aapl = api.get_bars("AAPL", TimeFrame.Minute, "2021-01-21", "2021-02-24", limit=5000, adjustment='raw').df
# A timeframe when $AAPL price was relatively flat
flat_aapl = api.get_bars("AAPL", TimeFrame.Minute, "2020-11-11", "2020-11-13", limit=5000, adjustment='raw').df

# ---> Test the bot with one of the timeframes (for example flat_aapl):
# ---> Just set close to a list of closing prices and run this cell. Example lists are provided by the Alpaca API above.
close = flat_aapl["close"].tolist()

async def run_test():
  for i in range (len(close)-1):
    await bot.tick(close[i], i)

  holding_comparison = close[len(close)-1] - close[0]
  print("Profit of the bot: " + str(bot.performance))
  print("Profit when just holding for comparison: " + str(holding_comparison))

asyncio.run(run_test())