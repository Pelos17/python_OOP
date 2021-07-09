class forniture:
    def __init__(self):
        self.tipo_madera = "Teakwood"

class chair(forniture):
    def __init__(self):
        super().__init__()
        self.__numeropatas = 4

    def crear_silla(self,tipo):
        if tipo == 1:
            print("Se creo la silla de madera {} con {} patas.".format(self.tipo_madera,self.__numeropatas))
        elif tipo == 2:
            self.tipo_madera = input("Ingrese que tipo de madera quiere para su silla\n")
            print("Se creo la silla de madera {} con {} patas.".format(self.tipo_madera,self.__numeropatas))
        

def menu():
    while True:
        print("Precione 1 para crear una silla extandard")
        print("Precione 2 para crear una silla de una madera especifica")
        print("Precione 3 para salir")
        opcion = int(input())
        silla = chair()
        if opcion == 1:
            silla.crear_silla(1)
        elif opcion == 2:
            silla.crear_silla(2)
        elif opcion == 3:
            print("Chau")
            quit()
        else:
            print("Opcion incorrecta")

menu()