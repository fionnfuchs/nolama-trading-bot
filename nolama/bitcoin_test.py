import alpaca_trade_api as tradeapi
from alpaca_trade_api.rest import TimeFrame
import nest_asyncio

from Historic_Crypto import HistoricalData

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from matplotlib.patches import Ellipse

from steps import BollingerBandsCalculation, BollingerBandsScoring
from bot import Bot

nest_asyncio.apply()

bot = Bot("BTC", None)
bot.calculation_steps.append(BollingerBandsCalculation(window=30, window_dev=2))
bot.scoring_steps.append(BollingerBandsScoring())

data = HistoricalData('BTC-USD',60,'2021-05-17-00-00','2021-05-19-00-00').retrieve_data()

close = data["close"].to_list()
print(close)

def run_test():
  for i in range (len(close)-1):
    bot.tick(close[i], i)

  holding_comparison = close[len(close)-1] - close[0]
  print("Profit of the bot: " + str(bot.performance))
  print("Profit when just holding for comparison: " + str(holding_comparison))

run_test()