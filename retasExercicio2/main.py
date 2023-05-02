#criar uma classe coeficiente angular e associar as retas ultilizadas para achar aquele coeficiente angular.
class CoeficienteAngular:
    def __init__(self,restricao1,coefAngular,restricao2):
        self.restricao1 = restricao1
        self.restricao2 = restricao2
        self.coefAngular = coefAngular    
class Restricao():
    def __init__(self, cordenadaX , cordenadaY, coeficiente):
        self.cordenadaX = cordenadaX 
        self.cordenadaY = cordenadaY
        self.coeficiente = coeficiente
        
    #calcula a intersecção da seguinte forma:
    #primeiro achamos o valor de x usando a seguinte formula " M1X1 + B1 = M2X2 + B2 "
    # que vai resulta em " M1X1-M2X2 = B2 -B1 " e por fim vai resultar em " X = B/M "
    # depois de acharmos o X eu subistitui o X na primeira equação no caso "M*valor de X + B"
class Pontos():

        def __init__(self, x , y,restricao1, restricao2=None):
            self.restricao1 = restricao1
            self.restricao2 = restricao2
            
            self.x = x 
            self.y = y
        

def calcularSistema(sistemas):
    # mx1 +b1 -z1 = mx2 +b2 -z2
    
    for sistema in sistemas:
        print(sistema)    
    
def solve_system_2x2(x1, y1, c1, x2, y2, c2):
    det = x1*y2 - x2*y1
    det_x = c1*y2 - c2*y1
    det_y = x1*c2 - x2*c1
    if det != 0:
        x = det_x / det
        y = det_y / det
        x = x*(-1)
        y = y*(-1)
        return (x, y)
    else:
        return 0 , 0

def acharInterseccao(coeficientes,pontos,restricoes):
    
    for i in range(len(coeficientes)):
      print("contador: "+str(i)+" coeficiente: "+str(coeficientes[i]))
      for j in range(len(coeficientes)):
        print("contador: "+str(j)+" coeficiente: "+str(coeficientes[j]))
        if i == j:
          print("")
        elif coeficientes[i] == coeficientes[j]:
          print("as retas são paralelas")
        elif coeficientes[i] != coeficientes[j]:
          print("as retas não são paralelas")
          x,y =solve_system_2x2(restricoes[i].cordenadaX,restricoes[i].cordenadaY,restricoes[i].coeficiente,restricoes[j].cordenadaX,restricoes[j].cordenadaY,restricoes[j].coeficiente,)          
          pontos.append(Pontos(x,y,restricoes[i],restricoes[j]))
        else:
            print("")

def coeficienteAngular(retas,coeficientes):
        for reta in retas:
            if reta.cordenadaX == 0:
                resultado = ""
            elif reta.cordenadaY == 0 :
                resultado = ""
                
            else:
                resultado = reta.cordenadaX/reta.cordenadaY
            coeficientes.append(resultado)
def exibirPontos(pontos):
    for ponto in pontos:
        if ponto.restricao2==None:
            print("retrição 1: "+str(ponto.restricao1.cordenadaX)+"  "+str(ponto.restricao1.cordenadaY))
            print("x: "+str(ponto.x)+" y: "+str(ponto.y))
            
        else:
            print("retrição 1: "+str(ponto.restricao1.cordenadaX)+"  "+str(ponto.restricao1.cordenadaY)+"  "+str(ponto.restricao1.coeficiente))
            print("retrição 2: "+str(ponto.restricao2.cordenadaX)+"  "+str(ponto.restricao2.cordenadaY)+"  "+str(ponto.restricao2.coeficiente))
            print("x: "+str(ponto.x)+" y: "+str(ponto.y))
            
def calcularPontosRetas(restricoes,pontos):
    for restricao in restricoes:
        y = -(restricao.coeficiente/restricao.cordenadaY)
        x = -(restricao.coeficiente/restricao.cordenadaX)
        pontos.append(Pontos(x,y,restricao)) 
def calcularFuncaoObjetiva(pontos, resultado):
    # e ruim pra comenta vo usar //
    #// para calculara função basta aplicala junto ao ponto em questão, no caso ficaria:
    #// transformar a função dada em equação.
    #// ex: 3x - y  --> 3.(x) - 1*(y), onde x e y pertencem ao ponto dado pelo limite.
    #// para equacao = [3,-1]
    for ponto in pontos:
        
        #// Faccin disse que o python não sabe regra de sinal então tem que dividir em duas variaveis.
        a = (ponto.restricao1.cordenadaX*ponto.x)
        b = (ponto.restricao1.cordenadaY*ponto.y)
        resultado.append(-(a + b))


restricoes  = []
coeficientes = []
pontos = []
sistema = []
resultados = []
# input para o usuario escolher os valores das retas NÃO DIGITE LETRAS DIGITE APENAS VALORES 
numeroRetas = int(input("quantas retas você quer criar ? "))
i = 0
while i < numeroRetas:        
    x = float(input("defina o valor de x da reta "+str(i+1)+" :  "))
    y = float(input("defina o valor de y da reta "+str(i+1)+" :  "))
    coeficiente = float(input("defina o valor do coeficiente da reta"+str(i+1)+" : "))
    restricoes.append(Restricao(x,y,coeficiente))
    print("x: " +str(restricoes[i].cordenadaX) + "  y: "+ str(+restricoes[i].cordenadaY)+"  restrição: "+ str(+restricoes[i].coeficiente))
    i+=1
    
    
calcularPontosRetas(restricoes,pontos)
coeficienteAngular(restricoes,coeficientes)
print("numero de coeficientes: "+str(len(coeficientes)))
print("numero de restricoes: "+str(len(restricoes)))
acharInterseccao(coeficientes,pontos,restricoes)
print("pontos de intersecção ")
exibirPontos(pontos)
calcularFuncaoObjetiva(pontos,resultados)
print("resultado do max")
for resultado in resultados:
    print(str(resultado))






