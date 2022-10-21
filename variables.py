
class FiguraGeometrica:
    def __init__(self,hancho,alto):
        self._hancho = hancho
        self._alto = alto

    @property
    def get_Alto(self):
         return self._alto
         
    @get_Alto.setter
    def set_Alto(self,alto):
        self._alto = alto

    @property
    def get_Hancho(self):
         return self._hancho

    @get_Hancho.setter
    def set_Hancho(self,hancho):
        self._hancho = hancho

    def __str__(self):
        return f'Figura geometrica Hancho:{self._hancho}, Alto:{self._alto}'

class Color:
    def __init__(self,color):
        self._color = color
    
    @property
    def get_Color(self):
         return self._color

    @get_Color.setter
    def set_Color(self,color):
        self._color = color
    
    def __str__(self):
        return f'El color selecionado es {self._color}'

class Cuadrado(FiguraGeometrica,Color):
    def __init__(self, lado,color):
        FiguraGeometrica.__init__(self,lado,lado)
        Color.__init__(self,color)

    def getArea(self):
        return self.get_Alto * self.get_Hancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} ,{Color.__str__(self)}'
        
cuadrado01 = Cuadrado(5,"rojo")
print(cuadrado01.getArea())
print(cuadrado01.__str__())




class Rectangulo(FiguraGeometrica,Color):
    def __init__(self, hancho, alto,color):
        FiguraGeometrica.__init__(self,hancho,alto)
        Color.__init__(self,color)

    def getArea(self):
        return self.get_Alto * self.get_Hancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} ,{Color.__str__(self)}'