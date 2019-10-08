import numpy as np
def pd_to_rate(pd_365, selic_360, margem_360):
    juros_tot_360 = (1 + selic_360)*(1 + margem_360)-1
    print('juros_tot_360 = ' + str('{0:.4%}'.format((juros_tot_360))))
    juros_tot_30 = (1 + juros_tot_360)**(1/12)-1
    print('juros_tot_30 = ' + str('{0:.4%}'.format((juros_tot_30))))
    xpmt = 1/(1/((1+juros_tot_30)**1)+1/((1+juros_tot_30)**2))
    adimp_1 = (1-pd_365)**(30/365)
    adimp_2 = (1-pd_365)**(60/365)

    print('xpmt = ' + str(xpmt))

    print('pd_365 = ' + str('{0:.4%}'.format(pd_365)))
    print('1-pd_365 = ' + str(1-pd_365))

    print('adimp_1 = ' + str(adimp_1))
    print('adimp_2 = ' + str(adimp_2))

    cf_1 = xpmt/adimp_1
    print('cf_1 = ' + str(cf_1))
    cf_2 = xpmt/adimp_2
    print('cf_2 = ' + str(cf_2))

    taxa_30 = np.irr([-1, cf_1, cf_2])
    taxa_30_1 = (1+juros_tot_30)/adimp_1-1
    taxa_30_2 = (1+juros_tot_30)/((1-pd_365)**(30/365))-1

    return taxa_30_2

print('{0:.10%}'.format(pd_to_rate(pd_365=0.595147715286786, selic_360=0.10, margem_360=0.0999685625032758)))
# 9.43966090378747%
# 9.4396609099%
