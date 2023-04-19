#classe onde vai ficar armazenado os pontos x e y das retas 
# e tambem vai fazer as operações para achar o coeficiente angular 
# e os pontos de intesecção
#-----------------------
class Reta:
    def __init__(self, x , y):
        self.x = x
        self.y = y
        
    #calcula a intersecção da seguinte forma:
    #primeiro achamos o valor de x usando a seguinte formula " M1X1 + B1 = M2X2 + B2 "
    # que vai resulta em " M1X1-M2X2 = B2 -B1 " e por fim vai resultar em " X = B/M "
    # depois de acharmos o X eu subistitui o X na primeira equação no caso "M*valor de X + B"     
    
    def calcularInterseccao(retas):
        x = Reta.calcularX(retas)
        y = Reta.calcularY(x, retas)
        
        print("pontos de intersecção: ( "+str(x)+" , "+str(y)+" )")    
        
    def calcularX(retas):
        coeficienteMX = []
        coeficienteB = []
        
        for reta in retas:
            print(retas)
            coeficienteMX.append(reta.x)
            coeficienteB.append(reta.y)
        m = calcularCoeficiente(coeficienteMX[1],coeficienteMX[0])
        b = calcularCoeficiente(coeficienteB[0],coeficienteB[1])
        return b/m
    
    
    def calcularY(x, retas):
        
        y = (retas[0].x*x)+retas[0].y
        return y 
    
   
        
    def coeficienteAngular(retas):
        coeficientes = []
        for reta in retas:
            coeficientes.append (float(reta.x/reta.y))
        return coeficientes
    
def calcularCoeficiente(coeficiente1,coeficient2):
    return coeficiente1 - coeficient2
          
def acharInterseccao(coeficientes):
    for i in range(len(coeficientes)):
      print("contador: "+str(i)+" coeficiente: "+str(coeficientes[i]))
      for j in range(len(coeficientes)):
        print("contador: "+str(j)+" coeficiente: "+str(coeficientes[j]))
        if i == j:
          print("")
        elif coeficientes[i] == coeficientes[j]:
          print("as retas são paralelas")
        else:
          print("as retas não são paralelas")
               


i = 0
retas  = []
coeficientes = []
# input para o usuario escolher os valores das retas NÃO DIGITE LETRAS DIGITE APENAS VALORES 
numeroRetas = int(input("quantas retas você quer criar"))
i = 0
while i < numeroRetas:        
    x = float(input("defina o valor de x da reta "+str(i+1)+" : "))
    y = float(input("defina o valor de y da reta"+str(i+1)+" : "))
    retas.append(Reta(x,y))
    print("x: " +str(retas[i].x) + " y: "+ str(+retas[i].y))
    i+=1
    
coeficientes = Reta.coeficienteAngular(retas)
acharInterseccao(coeficientes)


