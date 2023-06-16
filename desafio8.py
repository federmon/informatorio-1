from datetime import date

    
'''
Desafío 8: Principios de programación orientada a objetos
Requisitos técnicos:
- Herencia
- Encapsulamiento
Crear las siguientes clases con sus atributos y métodos.

Clase Usuario
 atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de
registro, avatar, estado, online
 métodos: login(), registrar(), logout() 

Clase Publico(Usuario)
 atributo: es_publico
 métodos: registrar(), comentar()

clase Colaborador(Usuario)
 atributos: es_colaborador
 métodos: registrar(), comentar(), publicar()

clase Articulo
 id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado

clase Comentario
 id, id_articulo, id_usuario, contenido, fecha_hora, estado
Código para elegir entre registrar usuarios o hacer login (si ya está registrado). Una vez registrado y
logueado, código que permita comentar al Publico y además publicar al Colaborador.

Clase Usuario V
Clase Publico V x
Clase Colaborador X
Clase Articulo X
Clase Comentario X
'''


class Usuario:
  def __init__(self):
    self.__id = None
    self.__nombre = None
    self.__apellido = None
    self.__telefono = None
    self.__username = None
    self.__email = None
    self.__contrasena = None
    self.__fecha = None
    self.__avatar = None
    self.__estado = None
    self.__online = None

    

  def set_id(self,id):
    self.__id=id
  def set_nombre(self,nombre):
    self.__nombre=nombre   
  def set_apellido(self,apellido):
    self.__apellido=apellido
  def set_telefono(self,telefono):
    self.__telefono=telefono
  def set_username(self,username):
    self.__username=username
  def set_email(self,email):
    self.__email=email
  def set_contrasena(self,contrasena):
    self.__contrasena=contrasena
  def set_fecha(self,fecha):
    self.__fecha=fecha
  def set_avatar(self,avatar):
    self.__avatar=avatar
  def set_estado(self,estado):
    self.__estado=estado
  def set_online(self,online):
    self.__online=online

  def login(self):
    self.set_online=True

  def logout(self):
    self.set_online=False

  def registrar(self,id,nombre,apellido,telefono,username,email,contrasena,avatar):
    self.set_id(id)
    self.set_nombre(nombre)
    self.set_apellido(apellido)
    self.set_telefono(telefono)
    self.set_username(username)
    self.set_email(email)
    self.set_contrasena(contrasena)
    self.set_avatar(avatar)
    self.set_estado(True)
    self.set_online(False)
    self.set_fecha(date.today())    
  def atributos(self):
    print(self.__id, ":", )
    print("Nombre", self.__nombre)
    print("Apellido", self.__apellido)
    print("Telefono", self.__telefono)
    print(self.__username)
    print(self.__email)
    print(self.__contrasena)
    print(self.__avatar)
    print("Estado", self.__estado)
    print(self.__online)
    print(self.__fecha)
class Publico(Usuario):
    def __init__(self):
        self.es_publico=None 
    
    def set_es_publico(self,valor):
        self.es_publico=valor #Consultar que tipo de valor
    
    def registrar(self,id,nombre,apellido,telefono,username,email,contrasena,avatar):
        super().registrar(id,nombre,apellido,telefono,username,email,contrasena,avatar)
        self.set_es_publico(True)
        
    def comentar(algo):
        print(algo)
        
        
        
class Colaborador(Usuario):
    def __init__(self):
        super().__init__()
        self.es_colaborador=None
    
    def atributos(self):
       return super().atributos()

    
    def set_es_colaborador(self,valor):
        self.es_colaborador=valor #Consultar que tipo de valor
    
    def registrar(self,id,nombre,apellido,telefono,username,email,contrasena,avatar):
        super().registrar(id,nombre,apellido,telefono,username,email,contrasena,avatar)
        self.set_es_colaborador(True)    
        
    def comentar(algo):
        print(algo)
        
    def publicar(algo):
        print(algo)


        
class Articulo:
    def __init__(self,id,id_usuario,titulo,resumen,contenido,fecha_publicacion,imagen,estado):
        self.id=id
        self.id_usuario=id_usuario
        self.titulo=titulo
        self.resumen=resumen
        self.contenido=contenido
        self.fecha_publicacion=fecha_publicacion
        self.imagen=imagen
        self.estado=estado
        
class Comentario:
    def __init__(self,id,id_articulo,id_usuario,contenido,fecha_hora,estado):
        self.id=id
        self.id_articulo=id_articulo
        self.id_usuario=id_usuario
        self.contenido=contenido
        self.fecha_hora=fecha_hora
        self.estado=estado

class Sistema:
    def __init__(self):
        print('Comienza el juego')
        
        colaborador1=Colaborador()
        colaborador1.registrar(1,'Fede','Monzon',3624123456,'fedemon','fedemon@gmail.com','123456',
            'www.tusfotos.com/fotodefede'
        )
        publico1=Publico()
        publico1.registrar(2,'Cristian','Moreira',3624654321,'crismor','crismor@gmail.com','654321c','www.tusfotos.com/fotodecris')
        self.usuarios= [colaborador1,publico1]
        colaborador1.atributos()
        self.comentarios=[]
        self.articulos=[]
    
   
    
    def comenzar(self):
        def ingresar_entero(mensaje,error):            
            while True:
                try:
                    numero = int(input(mensaje))
                    return numero
                except ValueError:
                    print(error)
        bandera = True
        
        while bandera:
            print("Que desea realizar? 1_ Registrar 2_Logearse 3_Salir")
            opcion=ingresar_entero('Ingresar la opcion: ','Por favor ingresa un numero nada mas')
            print
            if opcion==1:
                print('registrar()')
            elif opcion==2:
                print('loguearse()')
            else:
                bandera=False
                print('Esto fue el desafio_8 del grupo 3')
        







#Comienza el algoritmo                 
desafio8=Sistema()
desafio8.comenzar()       




'''

class Publico(Usuario):
  def __init__(self, id, nombre, apellido, telefono, username, email, contrasena, fecha, avatar, estado, online):
    super().__init__( id, nombre, apellido, telefono, username, email, contrasena, fecha, avatar, estado, online)
def registro( registrar(), comentar())

class Colaborador(Usuario)
      def_init_(self, "es_colaborador")
        super()_init_(id, nombre, apellido, telefono, username, email, contrasena, fecha, avatar, estado, online)

def registro(registrar(), comentar(), publicar())
bandera = True
usuarios = []
print('asdasd')
while bandera:
    print("Que desea realizar? 1_ Registrar 2_Logearse 3_Salir")
    opcion=ingresar_entero('Ingresar la opcion: ','Por favor ingresa un numero nada mas')
    if opcion == 1:
                registrar
            elif opcion == 2:
                loggearse:
            else:
                bandera=False
'''


        