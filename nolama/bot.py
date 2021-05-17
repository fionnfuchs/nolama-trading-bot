from alpaca import AlpacaAPIHandler
import pandas as pd

class Bot:
    """
    The core class of this project. Receives closing prices of the stock via the tick function, calculates TA values and buys / sells stocks based on a score.
    Look at the usage example for a quickstart.
    """

    def __init__(self, symbol, api, testing=True, crop_at=100, score_threshold=1):
        self.symbol = symbol
        self.testing = testing
        self.crop_at = crop_at
        self.score_threshold = score_threshold

        self.df = pd.DataFrame({"close": []})
        self.ta_values = []
        self.index = 0

        self.calculation_steps = []
        self.scoring_steps = []

        self.holding = False
        self.bought_at = 0.0
        self.performance = 0.0
        self.trades = []

        self.api_handler = AlpacaAPIHandler(api)

    def calculate_ta_values(self):
        """
        Calculate Technical Analysis values needed for the Bot to work and return them as a dictionary.
        """

        new_ta_values = {}

        for step in self.calculation_steps:
            new_ta_values = step.calculate(self.df, new_ta_values)

        self.ta_values.append(new_ta_values)

    def crop_stored_data(self):
        """
        Crop data stored by the bot.
        """
        if len(self.df.index) > self.crop_at:
            self.df = self.df.iloc[1:]
            self.ta_values.pop(0)

    def get_current_ta_values(self):
        """
        Return the last Technical Analysis value dictionary stored by the bot.
        """
        return self.ta_values[len(self.ta_values) - 1]

    def calculate_score(self, close):
        """
        Uses a list of ScoringSteps to calculate a score for the current values.

        :param close: The current closing price
        """
        score = 0

        for step in self.scoring_steps:
            score += step.get_score(score, {"ta_values": self.get_current_ta_values(), "close": close})

        return score

    def buy(self, close):
        """
        Trigger to buy the stock if currrently not holding.
        """
        if not self.holding:
            # print("--- Buying at " + str(close) + " ---")
            self.holding = True
            self.bought_at = close
            self.trades.append({"type": "buy", "price": close, "index": self.index})

            if not self.testing:
                self.api_handler.buy(self.symbol, 10)

    def sell(self, close):
        """
        Trigger to sell the stock if currrently not holding.
        """
        if self.holding:
            # print("    Selling at " + str(close))
            self.holding = False
            self.trades.append({"type": "sell", "price": close, "index": self.index})
            profit = close - self.bought_at
            self.performance += profit
            # print("    Profit so far: " + str(self.performance))

            if not self.testing:
                self.api_handler.sell(self.symbol, 10)

    def decide(self, score, close):
        """
        Decide if the stock should be bought or sold.
        """
        if score >= self.score_threshold:
            self.buy(close)
        elif score <= -self.score_threshold:
            self.sell(close)

    async def tick(self, close, index=0):
        """
        Async tick function. Called with a closing price. Updates all values, calculates score and calls bot actions.
        """
        close_value = pd.DataFrame({"close": [close]})
        self.df = self.df.append(close_value)
        self.crop_stored_data()

        self.calculate_ta_values()
        score = self.calculate_score(close)

        self.decide(score, close)
        self.index = index

