#variables de entrada

nombre= ""
puntaje=0
salario=0
edad=0


nombre = input("ingrese nombre completo: ")

#descuento por edad
edad = int(input("ingrese su edad: "))

if edad in [15,16,17,18]:
    print("su descuento por edad es del 25%")
    edad=25
elif edad in [19, 20, 21]:
    print("su descuento por edad es del 15%")
    edad=15
elif edad in [22, 23, 24, 25]:
    print("su descuento por edad es del 10%")
    edad=10
else:
    edad > 25
    print("No cuenta con descuento por edad")

#descuento por puntaje

puntaje=int(input("ingrese el puntaje del examen: "))

if puntaje >= 80 and puntaje <= 86:
    print("su descuento por puntaj es del 30%")
    puntaje=30
elif puntaje > 86 and puntaje < 91:
    print("su descuento por puntaje es del 35%")
    puntaje=35
elif puntaje >= 91 and puntaje > 96:
    print("su descuento por puntaje es del 40%")
    puntaje=40
elif puntaje >= 96:
    print("su descuento por puntaje es del 45%")
    puntaje=45
else:
    puntaje < 80
    print("no hay apoyo por puntaje de examen")

#descuento por salario
      
salario=float(input("ingrese el numero de smlv familiar: "))  

if salario <= 1:
    print("su descuento por salario es del 30%")
    salario=30
elif salario > 1 and salario <=2:
    print("su descuento por salario es del 20%")
    salario=20
elif salario > 2 and salario <=3:
    print("su descuento por salario es del 10%")
    salario=10

elif salario > 3 and salario <=4:
    print("su descuento por salario es del 5%")
    salario=5
else:
    print("no cuenta con descuento por salarios")

 
total= edad + puntaje + salario


print("su nombre es:  ", nombre)
print("su descuento por edad es del: ", edad, "%")
print("su descueto por puntaje es del: ", puntaje, "%")
print("su descuento por salarios es del: ", salario, "%")


print("su descuento total sobre la matricula es:  ", total, "%")

 
    
     
     
   

