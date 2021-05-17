import numpy as np

from ta.volatility import BollingerBands

class TAStep:
    def __init__(self):
        pass

    def calculate(self, context, target_dict):
        return target_dict

class ScoringStep:

    def __init__(self):
        pass

    def get_score(self, context):
        return 0


class BollingerBandsCalculation(TAStep):

    def __init__(self, window=30, window_dev=2):
        self.window = window
        self.window_dev = window_dev

    def calculate(self, context, target_dict):
        bb = BollingerBands(close=context["close"], window=self.window, window_dev=self.window_dev)
        bb_hband = bb.bollinger_hband().tolist()
        bb_hband = bb_hband[len(bb_hband) - 1]
        bb_lband = bb.bollinger_lband().tolist()
        bb_lband = bb_lband[len(bb_lband) - 1]

        target_dict["bb_hband"] = bb_hband
        target_dict["bb_lband"] = bb_lband

        return target_dict

class BollingerBandsScoring(ScoringStep):

  def get_score(self, score, context):
    if not np.isnan(context["ta_values"]["bb_hband"]) and not np.isnan(context["ta_values"]["bb_lband"]):
      if context["close"] > context["ta_values"]["bb_hband"]:
        score -= 1
      elif context["close"] < context["ta_values"]["bb_lband"]:
        score += 1
    return score