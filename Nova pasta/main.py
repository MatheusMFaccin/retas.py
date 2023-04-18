class Reta:
    def __init__(self, x , y):
        self.x = x
        self.y = y
def coeficienteAngular(reta):
    return float(reta.x/reta.y)

i = 0
retas  = []
coeficientes = []
while i < 2:       
    x = float(input("defina o x da reta : "))
    y = float(input("defina o y da reta: "))
    retas.append(Reta(x,y))
    print("x: " +str(retas[i].x) + " y: "+ str(+retas[i].y))
    
    i+=1


for reta in retas:
    coeficientes.append(coeficienteAngular(reta))

if coeficientes[0] == coeficientes[1]:
    print("as retas são paralelas") 
else:
    print("as retas não são paralelas")
