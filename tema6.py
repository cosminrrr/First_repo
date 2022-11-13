# 1.Clasa Cerc
# Atribute: raza, culoare
# Constructor pentru ambele atribute
# Metode:
# ● descrie_cerc() - va PRINTA culoarea și raza
# ● aria() - va RETURNA aria
# ● diametru()
# ● circumferinta()

class Cerc:
    pi=3.14
# constructor
    def __init__(self,raza,culoare):
        self.raza=raza
        self.culoare=culoare
#metode
    def descrie_cerc(self):
        print('Cercul are raza de ',self.raza, 'cm si are culoarea ', self.culoare)
    def aria(self):
        return float(self.pi)*int(self.raza)**2
    def diametru(self):
        return 2*int(self.raza)
    def circumferinta(self):
        return 2*float(self.pi)*int(self.raza)
#obiecte
cerc1=Cerc('7','alb')
cerc1.descrie_cerc()
print(cerc1.aria())
print(cerc1.diametru())
print(cerc1.circumferinta())

cerc2=Cerc('8','visiniu')
cerc2.descrie_cerc()
print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())


