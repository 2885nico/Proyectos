clave=input("ingrese una clave a encriptar: ")
largo=len(clave)

##inicializamos las variables a utilizar
k=0
pripri=0
crypted=''

##Iniciamos el ciclo
for i in clave:
  ##tomamos una letra de la clave
  print(i)
  
  ##tomamos el valor ASCII de la letra
  m=ord(i)
  print(m)
  
  ##elevamos el valor ASCII por la ubicacion de la letra en la clave partiendo por 0
  p= m**k
  print(p)
  
  ##transformamos el valor a cadena
  o=str(p)
  print(o)
  
  ##transformamos el valor de la cadena a hexadecimal
  l = int(o.encode().hex())
  print(l)
  
  ##generamos la cadena de la clave encriptada separando por guion
  crypted+=str(l)+'-'
  prin(tcrypted)
  
  ##generamos otra cadena de la clave encriptada pero sin guion
  pripri+=l
  print(str(pripri))

  ##aumentamos el contador
  k+=1
  
##print(crypted)
