class autos:
    #constructor
    def __init__(self,dicautos):
        self.autos = dicautos
    
    #muestro el catalogo de autos
    def catalogo(self):
        print("Autos Dispoinbibles!!!\n")
        print("MODELO/PRECIO\n")
        for auto in self.autos:
            print(auto," $",self.autos[auto])


    def renta(self,opcion,horas):
        try:

            total = self.autos[opcion] * horas
            return total
        except KeyError:
            print("Modelo Incorrecto")

rentacar = autos({"Hatchback":30,"Sedan":50,"SUV":100})


def menu():
    while True:
        print("\nBienvenido")
        print("Precione 1 para ver el catalogo")
        print("Precione 2 para calcular el costo del alquiler")
        print("precione 3 para salir del menu\n")
        menu = int(input())
        if menu == 1:
            rentacar.catalogo()
        elif menu == 2:
            modelo = input("Ingrese el modelo listado en el catalogo\n")
            try:
                horas = int(input("Ingrese la cantidad de horas que desea alquilar\n"))
                print(rentacar.renta(modelo,horas))
            except ValueError:
                print("\nLas horas deben ser ingresadas como numeros")
        elif menu == 3:
            print("Chau")
            quit()
        else:
            print("Opcion incorrecta")

menu()
