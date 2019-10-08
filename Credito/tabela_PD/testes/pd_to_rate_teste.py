from rate_to_pd import rate_to_pd
def pd_to_rate(pd_365, selic_360, margem_360):
    juros_tot_360 = (1 + selic_360)*(1 + margem_360)-1
    juros_tot_30 = (1 + juros_tot_360)**(1/12)-1
    taxa_30 = (1+juros_tot_30)/((1-pd_365)**(30/365))-1

    return taxa_30

pd_s_da_tabela = [0.595147715, 0.582069512, 0.461748899, 0.58160793, 0.445803637, 0.450750248, 0.581607931, 0.720325463, 0.95, 0.99]

for pd in pd_s_da_tabela:
    rate = pd_to_rate(pd_365=pd, selic_360=0.10, margem_360=0.0999685625032758)
    pd_reversa = rate_to_pd(rate, selic_360=0.10, margem_360=0.0999685625032758)
    print('{0:.10%}'.format(pd_to_rate(pd_365=pd, selic_360=0.10, margem_360=0.0999685625032758)))
    print(pd_reversa)
