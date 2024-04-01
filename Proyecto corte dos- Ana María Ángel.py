
class Producto:
    def __init__(self,Nombre,Descripcion,Precio,Cantidad_disponible):
        self.Nombre=Nombre
        self.Descripcion=Descripcion
        self.Precio=Precio
        self.Cantidad_disponible=Cantidad_disponible

class CarroDeCompras:
    instancia=None

    def __new__(clas):
        if clas.instancia is None:
            clas.instancia=super().__new__(clas)
            clas.instancia.Productos=[]
        return clas.instancia

    def agregar_Producto(self,Producto,Cantidad=1):
        for i in self.Productos:
            if i["Producto"]==Producto:
                i["Cantidad"]+=Cantidad
                break
        else:
            self.Productos.append({"Producto":Producto,"Cantidad": Cantidad})

    def eliminar_Producto(self,Producto):
        self.Productos=[i for i in self.Productos if i["Producto"] != Producto]

    def calcular_total(self):
        return sum(i["Producto"].Precio*i["Cantidad"] for i in self.Productos)

class Usuario:
    def __init__(self,Nombre):
        self.Nombre=Nombre
        self.Carro=CarroDeCompras()

    def agregar_al_Carro(self,Producto,Cantidad=1):
        if Cantidad<=Producto.Cantidad_disponible:
            self.Carro.agregar_Producto(Producto,Cantidad)
            print(f"{Cantidad}{Producto.Nombre}agregado al carro")
        else:
            print("La cantidad digitada no esta disponible")

    def ver_Carro(self):
        if not self.Carro.Productos:
            print("El carro esta vacio")
        else:
            print("Productos en el carro:")
            for i in self.Carro.Productos:
                Producto=i["Producto"]
                print(f"- {Producto.Nombre}:${Producto.Precio}x{i['Cantidad']}")
            print(f"Precio total:{self.Carro.calcular_total()}")

            
    def realizar_pedido(self):
        if not self.Carro.Productos:
            print("El Carro vacío")
            return

        total = self.Carro.calcular_total()
        print(f"Total del pedido: ${total}")

        direccion=input("Coloque su dirección de envio: ")
        tarjeta=input("Coloque su metodo de pago: ")
        print("Pedido confirmado")

     
        self.Carro.Productos=[] 

def main():
  
    PijamaSpiderman=Producto("Pijama de Spiderman","conjunto saco y pantalon, con telas suaves, este pijama ofrece la combinacion perfecta de comodidad y estilo", 85000,59)
    CobijaSpiderman=Producto("Cobija de Spiderman","tamaño Queen, con tela felpa, adornada con diseño de Spiderman", 105000, 35)
    AlmohadaSpiderman=Producto("Almohada de Spiderman","con materiales suaves, garantizando un apoyo comodo para tu cabeza y cuello", 58000, 20)
    PercianaSpiderman=Producto("Perciana de Spiderman","con materiales de alta calidad, duradera y fácil de instalar, con temática de Spiderman", 150000,25)

    
    Nombre_usuario=input("Coloque su nombre y apellido: ")
    usuario=Usuario(Nombre_usuario)

    while True:
        print("\n1. Ver Productos")
        print("2. Ver detalles de Productos")
        print("3. Agregar producto al Carro")
        print("4. Ver Carro")
        print("5. Realizar pedido")
        print("6. Terminar")

        opcion=input("Seleccione una opcion: ")

        if opcion=="1":
            print("\nProductos:")
            print(f"1.{PijamaSpiderman.Nombre}")
            print(f"2.{CobijaSpiderman.Nombre}")
            print(f"3.{AlmohadaSpiderman.Nombre}")
            print(f"4.{PercianaSpiderman.Nombre}")

        elif opcion=="2":
            print("\nDetalles de productos:")
            print(f"1.{PijamaSpiderman.Nombre}:{PijamaSpiderman.Descripcion},${PijamaSpiderman.Precio}")
            print(f"2.{CobijaSpiderman.Nombre}:{CobijaSpiderman.Descripcion},${CobijaSpiderman.Precio}")
            print(f"3.{AlmohadaSpiderman.Nombre}:{AlmohadaSpiderman.Descripcion},${AlmohadaSpiderman.Precio}")
            print(f"4.{PercianaSpiderman.Nombre}:{PercianaSpiderman.Descripcion},${PercianaSpiderman.Precio}")
        elif opcion=="3":
            print("\nProductos:")
            print(f"1.{PijamaSpiderman.Nombre}")
            print(f"2.{CobijaSpiderman.Nombre}")
            print(f"3.{AlmohadaSpiderman.Nombre}")
            print(f"4.{PercianaSpiderman.Nombre}")
            Producto_seleccionado=input("Coloque el número del producto que quiere agregar: ")
            Cantidad=int(input("Coloque la cantidad que quiere: "))
            if Producto_seleccionado=="1":
                usuario.agregar_al_Carro(PijamaSpiderman,Cantidad)
            elif Producto_seleccionado=="2":
                usuario.agregar_al_Carro(CobijaSpiderman,Cantidad)
            elif Producto_seleccionado=="3":
                usuario.agregar_al_Carro(AlmohadaSpiderman,Cantidad)
            elif Producto_seleccionado=="4":
                usuario.agregar_al_Carro(PercianaSpiderman,Cantidad)    
            else:
                print("El producto no existe")

        elif opcion=="4":
            usuario.ver_Carro()

        elif opcion=="5":
            usuario.realizar_pedido() 
            break

        elif opcion=="6":
            print("Gracias , hasta pronto")
            break
print("Bienvenidos a nuestra tienda ¡WilSpider!")
if __name__=="__main__":
    main()
