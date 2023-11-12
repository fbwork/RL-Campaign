import locale

import numpy as np

from campaign import Campaign

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')
NUM_AD_CAMPAIGNS = 8
NUM_CUSTOMERS = 10000000

campaigns = []


def try_campaign(campaign):
    if np.random.random() <= campaign.conversion_rate:
        campaign.sales += 1
    else:
        campaign.no_sales += 1


def create_campaign():
    for c in range(NUM_AD_CAMPAIGNS):
        campaigns.append(Campaign(c))
        e_c_p_t = campaigns[c].expected_profit_per_trial()
        print(
            f"Campaign {c}: Expected Profit Per Trial: {locale.currency(e_c_p_t, grouping=True)}")


def customer_campaign():
    for customer in range(NUM_CUSTOMERS):
        accepted_campaign_id = -1
        best_beta_value = -1
        for campaign in campaigns:
            campaign_beta_value = np.random.beta(campaign.actual_profit_per_trial() + 1., NUM_AD_CAMPAIGNS / 2.)
            if campaign_beta_value > best_beta_value:
                best_beta_value = campaign_beta_value
                accepted_campaign_id = campaign.id

        try_campaign(campaigns[accepted_campaign_id])
    total_profit_thompson_sampling = 0
    total_profit_uniform_sampling = 0
    uniform_customers_per_campaign = NUM_CUSTOMERS / NUM_AD_CAMPAIGNS

    for campaign in campaigns:
        print(
            f'Campaign {campaign.id}: Actual profit per trial = '
            f'{locale.currency(campaign.actual_profit_per_trial(), grouping=True)},'
            f' Total trials = {campaign.total_trials()}')
        total_profit_thompson_sampling += campaign.total_profit()
        total_profit_uniform_sampling += (
                uniform_customers_per_campaign * campaign.conversion_rate * campaign.average_profit_per_sale)

    print(
        '\nThompson Sampling total profit: {0}'.format(locale.currency(total_profit_thompson_sampling, grouping=True)))
    print('Uniform Sampling total profit: {0}'.format(locale.currency(total_profit_uniform_sampling, grouping=True)))
    print('Thompson Sampling absolute improvement: {0}'.format(
        locale.currency(total_profit_thompson_sampling - total_profit_uniform_sampling, grouping=True)))
    print('Thompson Sampling relative improvement: {0:.2%}'.format(
        (total_profit_thompson_sampling / total_profit_uniform_sampling) - 1.))


if __name__ == '__main__':
    create_campaign()
    customer_campaign()
