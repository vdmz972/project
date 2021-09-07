#2

class Road:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        self.weigth=25
        self.height=5

    def raschet_mass(self):
        mass_asph=self.length*self.weigth*self.weigth*self.height/1000
        print(f"Для покрытия нужно\n{round(mass_asph)}")


r=Road(5000,20)
r.raschet_mass()








