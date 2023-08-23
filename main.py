class Asiento:
    def init (self, color, precio,registro):
        self.color = color 
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self,newcolor):
        
        if ((newcolor == "rojo") or (newcolor == "verde") or (newcolor == "amarillo") or (newcolor == "negro") or (newcolor == "blanco") ) :
            self.color=newcolor


class Motor:
    def init (self, numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros 
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self,a):
        self.registro = a

    def asignarTipo(self,t):
        if((t == "electrico") or (t=="gasolina")):
            self.tipo=t

class Auto :
    cantidadCreados = 0
    def init (self,modelo,precio,asientos,marca,motor,registro,cantidadCreados):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro.registro
        
