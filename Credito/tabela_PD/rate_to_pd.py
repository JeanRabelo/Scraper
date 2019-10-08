def rate_to_pd(taxa_30, selic_360, margem_360):
    juros_tot_360 = (1 + selic_360)*(1 + margem_360)-1
    juros_tot_30 = (1 + juros_tot_360)**(1/12)-1
    taxa_30 = 1-((1+juros_tot_30)/(1+taxa_30))**(365/30)

    return taxa_30
