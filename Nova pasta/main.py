import matplotlib
from scipy.optimize import linprog






# max 2x-y
# 3x+4y<=0
# x+y>=2
# x>=0
# y>=0


# objetivo = [-2, 1]
# coefs = [[3, 4], [-1, -1]]
# results = [0, -2]
# limites = ((0, None), (0, None))


# resultado = linprog(
#     objetivo,
#     A_ub=coefs,
#     b_ub=results,
#     method='simplex',
#     bounds=limites

# )

coeficientesD = []
direitaDasRestricaoD =[]
teste = []
funcaoObjetivo = []
numeroRestricoes = int(input('digite o numero de restricoes'))


i = 0
j=0
while i < numeroRestricoes:        
    
    # sinal = input("digite o sinal do coeficiente ( >= , = , <= )")
   
    coeficientesD.append( float(input("defina o valor de x da reta {} :  ".format(i+1))))
    coeficientesD.append( float(input("defina o valor de y da reta {} :  ".format(i+1))))
    teste.append(tuple(coeficientesD))
    coeficientesD =[]
    direitaDasRestricaoD.append(float(input("defina o valor do coeficiente da reta {} : ".format(i+1))))
   
    i+=1
    
numeroFuncaoObjetivo = int(input('digite o numero de coeficientes da função objetivo '))

print(teste)

i = 0

# while i < numeroFuncaoObjetivo:
#     numeroFuncaoObjetivo.append(float(input("defina o valor do coeficiente {}".format(i+1))))
