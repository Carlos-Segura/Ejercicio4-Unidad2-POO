# class Ventana():
    
#     def __init__(self, titulo = 'Hola', xvs = 0, xvi = 500, yvs = 0, yvi = 500):
#         self.__titulo = titulo
#         self.__xvs = xvs
#         self.__xvi = xvi
#         self.__yvs = yvs
#         self.__yvi = yvi
        
#     def getTitulo(self):
#         return self.__titulo
    
#     def getAncho(self):
#         return self.__xvi - self.__xvs
    
#     def getAlto(self):
#         return self.__yvi - self.__yvs
    
#     def moverDerecha(self, desplazamiento = 1):
#         self.__xvs += desplazamiento
#         self.__xvi += desplazamiento
    
#     def moverIzquierda(self, desplazamiento = 1):
#         self.__xvs -= desplazamiento
#         self.__xvi -= desplazamiento  
    
#     def Subir(self, desplazamiento = 1):
#         self.__yvi += desplazamiento
#         self.__yvs += desplazamiento
    
#     def Bajar(self, desplazamiento = 1):
#         self.__yvi -= desplazamiento
#         self.__yvs -= desplazamiento    
        
# X = Ventana()
# X.moverDerecha()
# X.moverIzquierda()
# X.Subir()
# print("Ancho Ventana: ", X.getAncho(), "/ Alto Ventana: ", X.getAlto())

class Persona():
    
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
        
    def getNombre(self):
        return self.__nombre
    
    def getEdad(self):
        return self.__edad
    
    def __sub__(self, otro):
        return self.__edad - otro.getEdad()
    
a1 = Persona("Carlos", 24)
a2 = Persona("Matias", 22)
print(a2 - a1)