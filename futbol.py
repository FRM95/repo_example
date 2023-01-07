class equipoFutbol():
    def __init__(self, nombre, pais, año) -> None:
        self.nombre = nombre
        self.pais = pais
        self.año = año
    def get_attr(self):
        return f'El equipo {self.nombre} de {self.pais} se creó en {self.año}'

class Real_Madrid(equipoFutbol):
    def __init__(self, nombre, pais, año, presidente, ciudad) -> None:
        super().__init__(nombre, pais, año)
        self.presidente = presidente
        self.ciudad = ciudad

    def get_attr(self):
        a = super().get_attr()
        print(f'{a} en la ciudad {self.ciudad}, tiene de presidente a {self.presidente}')
    
    def add_Patrocinio(self, patrocinio):
        self.patrocinio = patrocinio

class equiposdeFutbol():
    def __init__(self) -> None:
        self.listadeequipos = []
    
    def getattr(self):
        print(self.listadeequipos)

    def addequipo(self, equipo: equipoFutbol):
        self.listadeequipos.append(equipo)
    

rm = Real_Madrid('Real Madrid', 'España', 1902, 'Florentino Perez', 'Madrid')
rm.get_attr()

lista = equiposdeFutbol()
lista.addequipo(rm)
lista.getattr()
