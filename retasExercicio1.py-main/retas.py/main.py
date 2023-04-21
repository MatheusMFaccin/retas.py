class Reta:
    def __init__(self, cordenadaX , cordenadaY):
        self.cordenadaX = cordenadaX 
        self.cordenadaY = cordenadaY
    def calcularInterseccao(retas):
        x = Reta.calcularX(retas)
        y = Reta.calcularY(x, retas)
        
        print("pontos de intersecção: ( "+str(x)+" , "+str(y)+" )")  
        return x , y  
        
    def calcularX(retas):
        coeficienteMX = []
        coeficienteB = []
        
        for reta in retas:
            print(retas)
            coeficienteMX.append(reta.cordenadaX)
            coeficienteB.append(reta.cordenadaY)
        m = calcularCoeficiente(coeficienteMX[1],coeficienteMX[0])
        b = calcularCoeficiente(coeficienteB[0],coeficienteB[1])
        return b/m
    
    
    def calcularY(x, retas):
        
        y = (retas[0].cordenadaX*x)+retas[0].cordenadaY
        return y 
    
   
        
    def coeficienteAngular(retas):
        coeficientes = []
        for reta in retas:
            if reta.cordenadaX == 0:
                resultado = ""
            elif reta.cordenadaY == 0 :
                resultado = ""
                
            else:
                resultado = reta.cordenadaX/reta.cordenadaY
            coeficientes.append (resultado)
        return coeficientes

class Restricao(Reta):
    def __init__(self, cordenadaX , cordenaday, coeficiente):
        super().__init__(cordenadaX,cordenaday)
        self.coeficiente = coeficiente
        
    #calcula a intersecção da seguinte forma:
    #primeiro achamos o valor de x usando a seguinte formula " M1X1 + B1 = M2X2 + B2 "
    # que vai resulta em " M1X1-M2X2 = B2 -B1 " e por fim vai resultar em " X = B/M "
    # depois de acharmos o X eu subistitui o X na primeira equação no caso "M*valor de X + B"
    
    
    
def calcularCoeficiente(coeficiente1,coeficient2):
    return coeficiente1 - coeficient2
          
def acharInterseccao(coeficientes, retas):
    for i in range(len(coeficientes)):  
      print("contador: "+str(i)+" coeficiente: "+str(coeficientes[i]))
      for j in range(len(coeficientes)): 
        print("contador: "+str(j)+" coeficiente: "+str(coeficientes[j]))
        if i == j:
          print("")
        elif coeficientes[i] == coeficientes[j]:
          print("as retas são paralelas")
        else:
          retasInterseccao = []
          pontos = []
          print("as retas não são paralelas")
          retasInterseccao.append(retas[i])
          retasInterseccao.append(retas[j])
          
          x , y = Reta.calcularInterseccao(retasInterseccao)
          pontos.append(Reta(x,y))
    return pontos          


i = 0
restricoes  = []
coeficientes = []
# input para o usuario escolher os valores das retas NÃO DIGITE LETRAS DIGITE APENAS VALORES 
numeroRetas = int(input("quantas retas você quer criar ? "))
i = 0
while i < numeroRetas:        
    x = float(input("defina o valor de x da reta "+str(i+1)+" :  "))
    y = float(input("defina o valor de y da reta "+str(i+1)+" :  "))
    coeficiente = float(input("defina o valor do coeficiente da reta"+str(i+1)+" : "))
    restricoes.append(Restricao(x,y,coeficiente))
    print("x: " +str(restricoes[i].cordenadaX) + " y: "+ str(+restricoes[i].cordenadaY)+"  restrição: "+ str(+restricoes[i].coeficiente))
    i+=1
    
coeficientes = Reta.coeficienteAngular(restricoes)
pontos = acharInterseccao(coeficientes, restricoes)
for ponto in pontos:
    print(ponto.cordenadaX,ponto.cordenadaY)



w
