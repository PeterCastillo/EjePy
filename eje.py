class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        # __atributo > estaremos indicando que sera privado y por ende no puede ser accedido desde fuera de la clase PRIVADO
        self.__ventas = []
        # _atributo > atributo PROTEGIDO en Python mas que todo funciona para cuando queremos utilizar este atributo con herencia
        self._precio_mayorista = 100
    
    def generar_venta(self, fecha, cliente, cantidad):
        # antes de agregar la venta validar si aun tenemos stock para dicha venta
        # TODO: primero ver si tenemos ventas , si hay iteramos esas ventas y sacamos cuanto de cantidad hemos vendido. Luego ver si ese numero es menor que la cantidad total (el atributo cantidad) si es mayor indicar que YA hemos sobregirado las ventas. Por ultimo a esa cantidad de productos vendidos sumar la cantidad entrante y ver si es menor o igual que la cantidad total, si lo es, entonces generar la venta, caso contrario, no permitir la venta e indicar que no hay stock suficiente. Si es que no hay el saldo suficiente indicar cuanto es lo que tenemos para vender (Hasta el proximo miercoles 26)
        if(self.cantidad>0):
            if(self.cantidad < cantidad):
                res = input(f'No contamos con el stock suficiente para cubrir su pedido, pero contamos con {self.cantidad}, desea continuar la compra?(si/no)')
                if(res == "si"):
                    cantidad = self.cantidad
                else:
                    print("Muchas gracias por su visita.")
                    return
            venta = {
            'fecha': fecha,
            'cliente': cliente,
            'cantidad': cantidad
            }
            self.cantidad -= cantidad
            self.__ventas.append(venta)
            print('Venta registrada exitosamente')
        else:
            print("Muchas gracias por su visita, pero no podremos cubrir su pedido por insuficiencia de stock.")
    
    def mostrar_ventas(self):
        ventaTotal= 0
        for venta in self.__ventas:
            ventaTotal += venta["cantidad"]
        print(ventaTotal)
        return self.__ventas


detergente = Producto(nombre='Detergente Sapito', precio=4.50, cantidad=50)

detergente.generar_venta(fecha='2022-10-19', cliente='Eduardo de Rivero', cantidad=10)
detergente.generar_venta(fecha='2022-10-29', cliente='Julissa Perez', cantidad=30)



print(detergente.mostrar_ventas())