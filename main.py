class Asiento:
    def __init__ (self, color, precio,registro):
        self.color = color 
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self,newcolor):
        
        if ((newcolor == "rojo") or (newcolor == "verde") or (newcolor == "amarillo") or (newcolor == "negro") or (newcolor == "blanco") ) :
            self.color=newcolor


class Motor:
    def ____init____ (self, numeroCilindros,tipo,registro):
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
    def __init__ (self,modelo,precio,asientos,marca,motor,registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro

    def cantidadAsientos(self):
        c=0
        for i in range(5):
            if (asientos[i] != None):
                c = c+1
        return c
    
    def verificarIntegridad(self):
        frase = "Auto original"
        if(self.registro != self.motor.registro):
            frase = "Las piezas no son originales"
        for i in range(5):
            if((self.asientos[i] != None ) and (self.asientos[i].registro != self.registro)):
                frase = "Las piezas no son originales"
        return frase