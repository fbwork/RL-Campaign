import numpy as np


class Campaign:
    def __init__(self, campaign_id):
        self.id = campaign_id
        self.conversion_rate = np.random.uniform(0.01, 0.2)
        self.average_profit_per_sale = np.random.uniform(100., 200.)
        self.sales = 0
        self.no_sales = 0

    def total_trials(self):
        return self.sales + self.no_sales

    def total_profit(self):
        return self.sales * self.average_profit_per_sale

    def actual_profit_per_trial(self):
        total_trials = self.total_trials()
        if total_trials > 0:
            return self.total_profit() / total_trials
        else:
            return 0.

    def expected_profit_per_trial(self):
        return self.conversion_rate * self.average_profit_per_sale

    def __str__(self):
        return f"Campaign ({self.id}): c_rate: {self.conversion_rate}, " \
               f"a_p_p_sale: {self.average_profit_per_sale}"
