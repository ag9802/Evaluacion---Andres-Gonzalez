import json

data = {"Ferreteria":[]}

with open ("test.json", 'w') as file:
   json.dump(data,file, indent= 2) 


opcion = int(input("¿Que accion desea realizar?"))

#1 almacenar
#2 leer
#3 Editar


if opcion == 2:
   with open("test.json", 'r') as file:
      data = json.load(file)
      print(data)

if opcion == 1:
        data={}
        with open ("test.json", 'r') as file:
            data  = json.load(file)

a = input("Ingresar el Nombre del producto:")
b = input("Ingresar la Descripcion:")
c = input("Ingresar el precio:")

data["Ferreteria"].append({"Nombre":a,"Descripcion":b, "Precio":c})

print(data)

with open ("test.json", 'w') as file:
        
    json.dump(data,file, indent= 2)

if opcion== 3:
   data={}
   with open("test.json", 'r') as file:
      data = json.load(file)

d = input('Ingrese el valor a editar:')

for d in data["Ferreteria"]:
    if d in data["Ferreteria"]:
        
        with open("test.json", 'w') as file:
                json.dump(data, file, indent= 2)

    a=input('Ingrese el nuevo Nombre del producto:')
    b=input('Ingrese una nueva Descripcion:')
    c=input('Ingrese un nuevo valor del Precio:')
        
        
data["Ferreteria"].append({"Nombre":a,"Descripcion":b, "Precio":c})
print(data)

with open ("test.json", 'w+') as file:
        
    json.dump(data,file, indent= 2)


   
        




