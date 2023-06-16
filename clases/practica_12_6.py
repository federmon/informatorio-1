class Titular:
    def __init__(self):
        self.nombre: None
        self.apellido:None
        self.edad:None
        self.__cuit:None
    
    def __set_cuit(self,cuit):
        if len(cuit)>=10:
            self.__cuit=cuit
        else:
            print("el cuit ingresado no tiene una longitud aceptada")
    
            
    def __get_cuit(self):
        return self.cuit
    
    
class Banco:
    def __init__(self,nombre):
        self.nombre= nombre
        self.__cuit = None
        
    def __set_cuit(self,cuit):
        if len(cuit)>=10:
            self.__cuit=cuit
        else:
            print("el cuit ingresado no tiene una longitud aceptada")
    
    def __get_cuit(self):
        return self.cuit
    
class CuentaBancaria(Titular,Banco):
    def __init__(self,nombre_banco,saldo=0):
        super().__init__()
        Banco.__init__(self,nombre_banco)
        self.saldo=saldo
    
    def depositar(self,monto):
        self.saldo+=monto
        
    def retirar(self,monto):
        if monto <= self.saldo:
            self.saldo-=monto