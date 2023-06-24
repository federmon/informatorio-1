from datetime import date
from datetime import datetime
   
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
        primer_comentario=Comentario(1,1,1,"Soy el Colaborador que creo este articulo",datetime.now().strftime("%d/%m/%Y %H:%M"),True)
        self.agregar_comentario(primer_comentario)
    
    def get_articulos(self):
        return self.articulos
    
    def get_comentarios(self):
        return self.comentarios
    
    def get_usernames(self):
        return self.usernames
    
    def get_usuarios(self):
        return self.usuarios
    
    def get_username_by_id(self,id_usuario):
        for usuario in self.get_usuarios():
            if usuario.get_id()==id_usuario:                
                return usuario.get_username()
    
    def agregar_usuario(self,usuario):
        self.usuarios.append(usuario)
    
    def agregar_username(self,username):
        self.usernames.append(username)
    
    def agregar_comentario(self,comentario):
        self.comentarios.append(comentario)
    
    def agregar_articulo(self,articulo):
        self.articulos.append(articulo)
        
    def listar_articulos(self):
        articulos=self.get_articulos()
        for articulo in articulos:
            print(f"ID: {articulo.get_id()}, Titulo: {articulo.get_titulo()}")
        return(len(articulos))
    
    def listar_comentarios(self,id_articulo):
        #TODO Muestra por pantalla todos los comentarios o ninguno de un articulo
        pass

    def ingresar_entero(self,min,max,mensaje,error):            
            while True:
                try:
                    numero = int(input(mensaje))
                    if numero < min or numero > max:
                        raise ValueError
                    return numero
                except ValueError:
                    print(error)
    
    def crearArticulo(self,id_usuario):
        id_articulo=len(self.get_articulos())+1
        titulo=input("Por favor ingrese el titulo de su nevo Articulo: ")
        resumen=input("Por favor ingrese el resumen de su nuevo Articulo: ")    
        contenido=input("Ingrese el contenido de su Articulo")
        fecha_publicacion=datetime.today()
        imagen=input("ingrese el link de la imagen de su Articulo")
        estado=True
        nuevo_articulo=Articulo(id_articulo,id_usuario,titulo,resumen,contenido,fecha_publicacion,imagen,estado)
        print("nuevo articulo creado con éxito")
        return nuevo_articulo
    
    def crearComentario(self,id_articulo,id_usuario):
        contenido=input("Ingrese lo que opina respecto al articulo por favor: ")
        id_comentario=len(self.get_comentarios())+1
        estado=True
        fecha_hora= datetime.now().strftime("%d/%m/%Y %H:%M")
        print("momento creado: ", fecha_hora)
        comentario_nuevo=Comentario(id_comentario,id_articulo,id_usuario,contenido,fecha_hora,estado)
        return comentario_nuevo

    def leerComentarios(self,id_articulo):
        comentarios_del_articulo=[]
        for comentario in self.get_comentarios():
            if comentario.get_id_articulo() == id_articulo:
                comentarios_del_articulo.append(comentario)
        print("----------------------------------------")
        if len(comentarios_del_articulo)==0:
            print("No hay ningun comentario para el articulo que consulta")
            print("----------------------------------------")
        else:
            for comentario in comentarios_del_articulo:
                print(f"'{self.get_username_by_id(comentario.get_id_usuario())}' comentó: {comentario.get_contenido()}")
                print(f"fecha: {comentario.get_fecha_hora()}")
                print("----------------------------------------")
            
            
                    

        
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
        print(f'el usuario {username} ah sido registrado correctamente')
        
    def menu_opciones(self,username):
        while True:
            for user in self.get_usuarios():
                if user.get_username()==username:
                    usuario=user
            usuario.login()
            min=0
            max=1
            print(f"Bienvenido {usuario.get_nombre()}! que desea hacer? Usted es un usuario tipo: {type(usuario).__name__}")
            print("0_ Salir al Menu principal")
            print("1_ Leer Articulos")
            if 	type(usuario).__name__ == "Colaborador":
                max=2
                print("2_ Crear Articulo")
                
            opcion=self.ingresar_entero(min,max,"Por favor ingrese su respuesta: ",f"solamente ingrese desde {min} hasta {max}")
            if opcion==0:
                usuario.logout()
                self.comenzar()
                
            elif opcion==1:
                nro_articulos=self.listar_articulos()
                print(f"Desea leer los comentarios de alguno de los {nro_articulos} Articulos?")
                opcion=self.ingresar_entero(0,nro_articulos,"Por favor ingresa el id del articulo o 0 si desea salir: ",f"solamente ingrese desde 0 hasta {nro_articulos}")
                if opcion != 0:
                    self.leerComentarios(opcion)
                    id_articulo=opcion
                    opcion=self.ingresar_entero(0,nro_articulos,"Por favor ingresa 0 si desea salir o 1 si desea agregar un comentario: ","solamente ingrese 0 o 1")
                    if opcion == 1:
                        comentario=self.crearComentario(id_articulo,usuario.get_id())
                        self.agregar_comentario(comentario)
            else:
                articulo=self.crearArticulo(usuario.get_id())
                self.agregar_articulo(articulo)
                
        
        
    
    def validacion_username(self,username_valido):
        for username in self.get_usernames():
            if username==username_valido:
                return True
        return False
    
    def validacion_password(self,username_valido,password_valido):
        for usuario in self.get_usuarios():
            if usuario.get_username()==username_valido:
                if usuario.get_contrasena()==password_valido:
                    return True
                else:
                    return False
        return False
            
    
    def loguearse(self):
        while True:
            username=input('Ingrese su username por favor: ')
            if not self.validacion_username(username):
                print("El username ingresado es incorrecto por favor")
                opcion=self.ingresar_entero(1,2,'Desea intentar de nuevo ingrese 1 o ingrese 2 si desea salir al menu anterior: ','Por favor ingresa un numero del 1 o 2')
                if opcion==2:
                    break
            else:
                password=input("Perfecto, ahora ingrese su contraseña: ")
                if not self.validacion_password(username,password):
                    input("Contraseña incorrecta! Presiona ENTER para continuar")
                else:
                    input("contraseña correcta! Presiona ENTER para continuar")
                    self.menu_opciones(username) #acá ya esta logeado y entra en el menu
					
    
    def comenzar(self):
       
        bandera = True
        
        while bandera:
            print("------------------ Bienvenido al desafio 8 del grupo 3 ------------")
            print("Que desea realizar? 1_ Registrar 2_Logearse 3_Ver usuarios 4_ Salir")
            opcion=self.ingresar_entero(1,4,'Ingresar la opcion: ','Por favor ingresa un numero del 1 al 3')
            if opcion==1:
                print('---------------------------------- Inicio de Registracion ----------------------------------')
                self.registrar()                
            elif opcion==2:
                self.loguearse()
            elif opcion==3:
                print("USUARIOS CARGADOS: ")
                for index,username in enumerate (self.usernames,1):
                    print(index,username)
            else:
                bandera=False
                print('Esto fue el desafio_8 del grupo 3')
                quit
        







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


        