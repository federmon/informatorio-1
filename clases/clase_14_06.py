'''
Ejercicio 1: Pizzería
    Una pizzería de la ciudad ofrece a sus clientes una amplia variedad de pizzas de
    fabricación propia, de varios tamaños (8, 10 y 12 porciones).
    Los clientes tienen a disposición un menú que describe para cada una de las
    variedades, el nombre, los ingredientes y el precio según el tamaño y el tipo (a la
    piedra, a la parrilla, de molde) de la pizza. Los clientes realizan sus pedidos en el
    mostrador. 
    El pedido debe contener el nombre del Cliente, para llamarlo cuando
    su pedido está listo; la cantidad de pizzas, el tamaño, la variedad, la fecha del
    pedido, la hora en la que el pedido debe entregarse y la demora estimada
    informada al cliente. 
    El pedido va a la cocina y cuando está preparado se informa
    al que lo tomó para que se genere la factura correspondiente y se le entregue el
    pedido al cliente.
    
    El dueño de la pizzería ha manifestado la necesidad de acceder al menos a la
    siguiente información:
        
Variedades y tipos de pizzas más pedidas por los clientes.
Ingresos (recaudaciones) por períodos de tiempo.
Pedidos (cantidad y monto) por períodos de tiempo.

Primer ejercicio !

tamaños 1 chico, 2 mediano y 3 grande
tipo 1 parrilla 2 piedra y 3 molde

'''
        

class Pizza:
    def __init__(self,tamano,nombre,ingrendientes,tipo):
        self.tamano=tamano
        self.nombre=nombre
        self.ingrendientes=ingrendientes
        self.tipo=tipo
        self.precio=tamano*tipo
    
class Cliente:
    def __init__(self,nombre):
        self.nombre=nombre
        
    def get_cliente(self):
        return self.nombre
    def set_cliente(self,nombre):
        self.nombre=nombre
    

class Pedido():
    def __init__(self,id,fecha,nombre_cliente,demora,hora_actual,tamano,nombre,ingrendientes,tipo):
        self.id=id
        self.fecha=fecha
        self.cliente=Cliente(nombre_cliente)
        self.demora=demora
        self.hora_entrega=hora_actual+demora
        self.pizzas=[]
        primer_pizza=Pizza(tamano,nombre,ingrendientes,tipo)
        self.pizzas.append(primer_pizza)
        self.precio_pedido=primer_pizza.precio
        
    def cargar_pizza(self,tamano,nombre,ingrendientes,tipo):
        nueva_pizza=Pizza(tamano,nombre,ingrendientes,tipo)
        self.pizzas.append(nueva_pizza)
        self.demora+=1
        self.precio_pedido+=nueva_pizza.precio #crear setter
        
    def get_pedido(self):
        print(f'El pedido de:{self.cliente.get_cliente()} id:{self.id}, pizzas:{self.pizzas}\n')
        cant=1
        for pizza in self.pizzas:
            print(f'{cant}: nombre:{pizza.nombre}, precio:{pizza.precio}, tipo:{pizza.tipo}, ingredientes:{pizza.ingrendientes}')
            cant+=1
    
    def get_factura(self):
        print(f'El precio total de su pedido es: ${self.precio_pedido}')
        
        
pedido_cristian=Pedido(1,'14-6-23','Cristian',1,16,3,'Muzzarella',2,2)

pedido_cristian.cargar_pizza(3,'Muzzarella',2,2)
pedido_cristian.cargar_pizza(3,'Napolitana',3,1)
pedido_cristian.get_pedido()




    
    
        
    
        
        