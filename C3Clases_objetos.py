class empleado:
    name = "Pedro"
    def changename(self):
        self.name = input("Ingresa el nuevo nombre:\n")

pedro = empleado()
pedro.changename()
print(pedro.name)