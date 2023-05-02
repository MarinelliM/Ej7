class Viajero:
    num_viajero: int
    dni: str
    nombre: str
    apellido: str
    millas_acum: int


    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum) -> None:
        self.num_viajero = num_viajero
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.millas_acum = millas_acum
        pass

    def getmillas(self):
        return self.millas_acum
    
    def getnombrecompleto(self):
        return self.nombre + ' ' +self.apellido

    def acumularMillas(self, entero):
        self.millas_acum += entero
        print('Sus millas se acumularon con exito, sus millas actuales son {}' .format(self.getmillas()))

    def getnumv(self):
        return self.num_viajero
    
    def __gt__(self, otro):
        return self.getmillas() > otro.getmillas()
    
    def __add__(self, otro):
        return (self.getmillas() + otro)
    #def __add__(self, otro):
    #   return self.getmillas() + otro.getmillas()
    def __radd__(self, otro):
        return self.getmillas() + otro
    
    def __sub__(self,otro):
        return self.getmillas() - otro
    #def __sub__(self, otro):
    #   return self.getmillas() - otro.getmillas()
    def __rsub__(self,otro):
        return self.getmillas() - otro
    
    def __eq__(self, otro):
        return self.getmillas() == otro
    #def __eq__(self, otro):
    #   return self.getmillas() == otro.getmillas()
    def __req__(self, otro):
        return self.getmillas() == otro
    

    def canjearMillas(self, millascanje):
        if millascanje <= self.millas_acum:
            self.millas_acum = self.millas_acum - millascanje
            print('millas canjeadas con exito, sus millas actuales son {}' .format(self.getmillas()))
        else: return print('Sus millas son insuficientes')
