from sympy import Symbol, exp, integrate

# variáveis gerais
x=Symbol('x')
z=Symbol('z')
pi=Symbol('pi')

# constantes
mu1=Symbol('mu1'); mu2=Symbol('mu2')
sigma1=Symbol('sigma1'); sigma2=Symbol('sigma2')

y1=(1/(mu1*(2*pi)**(1/2)))*exp(((x-mu1)/sigma1)**2/2)
y2=(1/(mu2*(2*pi)**(1/2)))*exp(((z-x-mu2)/sigma2)**2/2)


print(y1);print(y2);print(y1*y2)


# sum = integrate(y1*y2,x)

# print(sum)
# print(sigma1)
