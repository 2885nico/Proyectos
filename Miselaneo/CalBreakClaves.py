#calcular tiempo de decifrado
largoClave=int(input("Ingrese largo de la clave: "))
numeroHilos=int(input("Ingrese cantidad de hilos para procesar: "))
nClavesN = 10**largoClave
nClavesC = 52**largoClave
nClavesCN = 62**largoClave
nClavesASCII = 95**largoClave
nClavesASCIIEXT = 222**largoClave
tiempoN = ((nClavesN)*0.001)/numeroHilos
tiempoC = ((nClavesC)*0.001)/numeroHilos
tiempoCN = ((nClavesCN)*0.001)/numeroHilos
tiempoASCII = ((nClavesASCII)*0.001)/numeroHilos
tiempoASCIIEXT= ((nClavesASCIIEXT)*0.001)/numeroHilos

print("Solo numeros: tiempo: "+str(tiempoN)+" segundos --> "+str(tiempoN/3600)+" horas.")
print("\t numero claves: "+str(nClavesN)+"\n")
print("Solo caracteres: tiempo: "+str(tiempoC)+" segundos --> "+str(tiempoC/3600)+" horas.")
print("\t numero claves: "+str(nClavesC)+"\n")
print("Caracteres y numeros: tiempo: "+str(tiempoCN)+" segundos --> "+str(tiempoCN/3600)+" horas.")
print("\t numero claves: "+str(nClavesCN)+"\n")
print("Caracteres ASCII: "+str(tiempoASCII)+" segundos --> "+str(tiempoASCII/3600)+" horas.")
print("\t numero claves: "+str(nClavesASCII)+"\n")
print("Caracteres ASCII + Extendido: tiempo: "+str(tiempoASCIIEXT)+" segundos --> "+str(tiempoASCIIEXT/3600)+" horas.")
print("\t numero claves: "+str(nClavesASCIIEXT)+"\n")
