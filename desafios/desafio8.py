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
    
  def get_id(self):
    return(self.__id)
  def get_nombre(self):
    return(self.__nombre)   
  def get_apellido(self):
    return(self.__apellido)
  def get_telefono(self):
    return(self.__telefono)
  def get_username(self):
    return(self.__username)
  def get_email(self):
    return(self.__email)
  def get_contrasena(self):
    return(self.__contrasena)
  def get_fecha(self):
    return(self.__fecha)
  def get_avatar(self):
    return(self.__avatar)
  def get_estado(self):
    return(self.__estado)
  def get_online(self):
    return(self.__online)

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
    print("ID: ",self.__id)
    print("Nombre: ", self.__nombre)
    print("Apellido: ", self.__apellido)
    print("Telefono: ", self.__telefono)
    print("Username: ",self.__username)
    print("Email: ",self.__email)
    print("Contraseña: ",self.__contrasena)
    print("Avatar: ",self.__avatar)
    print("Estado: ", self.__estado)
    print("Online: ",self.__online)
    print("Fecha de Alta: ",self.__fecha)
    
class Publico(Usuario):
    def __init__(self):
        self.es_publico=None 
    
    def get_es_publico(self):
        return self.es_publico()
    
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
        
    def get_id(self):
        return self.id
    def get_id_usuario(self):
        return self.id_usuario
    def get_titulo(self):
        return self.titulo
    def get_resumen(self):
        return self.resumen
    def get_contenido(self):
        return self.contenido
    def get_fecha_publicacion(self):
        return self.fecha_publicacion
    def get_imagen(self):
        return self.imagen
    def get_estado(self):
        return self.estado
        
class Comentario:
    def __init__(self,id,id_articulo,id_usuario,contenido,fecha_hora,estado):
        self.id=id
        self.id_articulo=id_articulo
        self.id_usuario=id_usuario
        self.contenido=contenido
        self.fecha_hora=fecha_hora
        self.estado=estado
        
    def get_id(self):
        return self.id
    def get_id_articulo(self):
        return self.id_articulo
    def get_id_usuario(self):
        return self.id_usuario
    def get_contenido(self):
        return self.contenido
    def get_fecha_hora(self):
        return self.fecha_hora
    def get_estado(self):
        return self.estado


class Sistema:  
    def __init__(self):
        print('Comienza el juego')
        #Cargamos 1 colaborador, 1 publico, 1 articulo y 1 comentario
        colaborador1=Colaborador()
        colaborador1.registrar(1,'Fede','Monzon',3624123456,'fedemon','fedemon@gmail.com','123456','www.tusfotos.com/fotodefede')
        publico1=Publico()
        publico1.registrar(2,'Cristian','Moreira',3624654321,'crismor','crismor@gmail.com','654321c','www.tusfotos.com/fotodecris')
        self.usuarios= []
        self.agregar_usuario(colaborador1)
        self.agregar_usuario(publico1)
        self.usernames=[]#se cargan los nombres en una lista para consultar cuando se registran si los usernames estan ocupados
        self.agregar_username(publico1.get_username())
        self.agregar_username(colaborador1.get_username())
        self.articulos=[]
        self.comentarios=[]
        #Creamos el primer Articulo
        primer_articulo=Articulo(1,1,"Titulo del Primer Articulo","Resumen del primer articulo","Contenido del primer articulo",date.today(),'www.imagen.com/primer_articulo',True)
        self.agregar_articulo(primer_articulo)
        #Creamos el primer Comentario del Primer Articulo
        
        
        
    def agregar_usuario(self,usuario):
        self.usuarios.append(usuario)
    
    def agregar_username(self,username):
        self.usernames.append(username)
    
    def agregar_comentario(self,comentario):
        self.comentarios.append(comentario)
    
    def agregar_articulo(self,articulo):
        self.articulos.append(articulo)
    

    def ingresar_entero(self,min,max,mensaje,error):            
            while True:
                try:
                    numero = int(input(mensaje))
                    if numero < min or numero > max:
                        raise ValueError
                    return numero
                except ValueError:
                    print(error)
                    

        
    def registrar(self):
        nuevo_username=input('Ingresar un username nuevo para poder crearse un usuario: ')
        if self.usernames.count(nuevo_username)==0:
            opcion=self.ingresar_entero(1,2,'Ingrese 1 si es un Usuario tipo Publico o 2 si es tipo Colaborador: ','Por Favor ingrese 1 o 2 nada más')
            if opcion==1:
                nuevo_user=Publico()
            else:
                nuevo_user=Colaborador()
            id=len(self.usuarios)+1
            nombre=input("Ingrese su nombre por favor: ")
            apellido=input('ingrese su apellido por favor: ')
            telefono=self.ingresar_entero(1,9999999999,'Ingrese su numero de telefono sin el 15','Por favor ingrese numeros nada mas: ')
            username=nuevo_username
            email=input("ingrese su correo electronico por favor: ")
            contrasena=input("Ingrese su contrasena por favor: ")
            avatar=input("ingrese el link de la imagen de su avatar: ")
            nuevo_user.registrar(id,nombre,apellido,telefono,username,email,contrasena,avatar)
            self.agregar_username(username)
            self.agregar_usuario(nuevo_user)
            self.usuarios.append(nuevo_user)
            print("Los Datos cargados del nuevo usuario son:")
            nuevo_user.atributos()
       	 #publico1.registrar(2,'Cristian','Moreira',3624654321,'crismor','crismor@gmail.com','654321c','www.tusfotos.com/fotodecris')
            input('Presiona Enter para continuar')
          
          
        else:
            while True:
                opcion=self.ingresar_entero(1,2,'Usuario ya ocupado. Que desea hacer? 1_ Probar otro usuario o 2_ Salir al menu anterior','Ingrese 1 o 2 nada mas por favor')
                if opcion == 1:
                    self.registrar()
                    break
                else:
                    break
                    
        print('finaliza metodo registar')
          
    
    
    def loguearse(self):
      pass
   
    
    def comenzar(self):
       
        bandera = True
        
        while bandera:
            print("Que desea realizar? 1_ Registrar 2_Logearse 3_Ver usuarios 4_ Salir")
            opcion=self.ingresar_entero(1,4,'Ingresar la opcion: ','Por favor ingresa un numero del 1 al 3')
            if opcion==1:
                print('---------------------------------- Inicio de Registracion ----------------------------------')
                self.registrar()
                
            elif opcion==2:
                print('loguearse()')
                input('Presione enter para continuar')
            elif opcion==3:
                print("USUARIOS CARGADOS: ")
                for index,username in enumerate (self.usernames,1):
                    print(index,username)
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


        