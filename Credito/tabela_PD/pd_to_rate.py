def pd_to_rate(pd_365, selic_360, margem_360):
    juros_tot_360 = (1 + selic_360)*(1 + margem_360)-1
    juros_tot_30 = (1 + juros_tot_360)**(1/12)-1
    taxa_30 = (1+juros_tot_30)/((1-pd_365)**(30/365))-1

    return taxa_30
