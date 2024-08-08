class animal:
    def __init__(self, nombre, peso):
        self.nombre= nombre
        self.pesos= peso 
        
    def printnombre(self):
        print(f"El nombre del animal es: {self.nombre, self.pesos}")
        
x = animal("Ryan",126)
x.printnombre()