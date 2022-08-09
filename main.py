#Pregunta 1:

#Declara una variable en python e imprimela por pantalla:

#nombre = "Noelia Gaona Andreu"
#print(nombre)

#Pregunta 2:

#Haz un bucle que imprima los números del 1 al 100:

#for i in range (1,101):
    #print(i)

#Pregunta 3:

#Crea una estructura if/else dentro del bucle para que esta imprima "Hola" cuando el número sea 5:

#for i in range (1,101):
#   if i == 5 :
#       print("Hola")
#   else:
#        print(i)

#Pregunta 4: FizzBuzz

#Escribe un programa que muestre por pantalla los números del 1 al 100 y que tenga en cuenta los siguientes casos especiales:

#1. Si el número es múltiplo de 3, mostrar por pantalla el número más la palabra "Fizz"
#2. Si el número es múltiplo de 5, mostrar por pantalla el número más la palabra "Buzz"
#3. Si el número es múltiplo de 3 y 5 a la vez, mostrar por pantalla el número más la palabra "FizzBuzz"
#4. Si no cumple ninguna de las anteriores, mostrar por pantalla solo el número

for i in range (1,101):
    if (i % 3)==0:
        print (i, str("Fizz"))
    if (i % 5)==0:
        print(i, ("Buzz"))
    if (i % 5 ) & (i % 3)==0:
        print(i, ("FizzBuzz"))
    else:
        print(i)