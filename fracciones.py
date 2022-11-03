#clase-python
class Fraction:
    #atributos#
    numerator=0
    denominator=1
    

    
    #fin seccion atributos#
    
   def __init__(self,numerador,denominador):
       self.numerator=numerador
       self.denominator=denominador
   
   def print(self): #voy a imprimir el numerador y denominador con un slash numerador/denominador
       print(self.numerator,"/",self.denominator)
        
   def multiplication(self,b)
       numerator=self.numerator*b.numerator
       denominator=self.denominator*b.denominator
       r=fraction(numerator,denominator)
       r=print()
      
a=fraction(3,2)
b=fraction(6,5)
a.print()
b.print()
a.multiplication(b)
       
      
#numerador=4
#denominador=5
o=fraction(4,5)
print(o.numerator)
print(o.denominator)
