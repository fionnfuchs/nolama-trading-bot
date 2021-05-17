class AlpacaAPIHandler():
    def __init__(self, api):
        self.api = api

    def buy(self, symbol, quantity):
        result = self.api.submit_order(
          symbol=symbol,
          qty=str(quantity),
          side='buy',
          type='market',
          time_in_force='gtc'
        )
    def sell(self, symbol, quantity):
        result = self.api.submit_order(
          symbol=symbol,
          qty=str(quantity),
          side='sell',
          type='market',
          time_in_force='gtc'
        )