import random

guerrero = ["Martillo", "Fuego", "Escudo", "Valor"]
guerrera = ["Espada", "Sangre", "Gloria", "Lucha"]

hechicero = ["Hechizo", "Saber", "Encantamiento", "Rayo"]
hechicera = ["Vara", "Magia", "Sabiduría", "Energía", "Esencia"]

arquero = ["Arco", "Viento", "Disparo", "Sombrío", "Sigilo"]
arquera = ["Flecha", "Precisión", "Sombra", "Destreza", "Puntería", "Centella", "Saeta"]

adjetivos_fem = ["Divertida", "Chiflada", "Bromista", "Despistada", "Risueña", "Alocada", "Traviesa", "Payasa", "Juguetona", "Tronchante"]

adjetivos_masc = ["Divertido", "Chiflado", "Bromista", "Despistado", "Risueño", "Alocado", "Travieso", "Payaso", "Juguetón","Tronchante"]

asig_titulosh=random.randint(0,3)
asig_adjectivosh=random.randint(0,9)

genero=str(input("Que genero quieres ser?(eri gei?): ")).upper()
trabajo=str(input("Que trabajo quieres ejercer?: ")).upper()

if genero=='MASCULINO':
  print(trabajo)
  if trabajo=='GUERRERO':
    print(guerrero[asig_titulosh],adjetivos_masc[asig_adjectivosh])
  elif trabajo=='HECHICERO':
    print(hechicero[asig_titulosh],adjetivos_masc[asig_adjectivosh])
  elif trabajo == 'ARQUERO':
    print(arquero[asig_titulosh],adjetivos_masc[asig_adjectivosh])
  else:
    print("eri gei?")

elif genero == 'FEMENINO':
  print(trabajo)
  if trabajo=='GUERRERA':
    print(guerrera[asig_titulosh],adjetivos_fem[asig_adjectivosh])
  elif trabajo=='HECHICERA':
    print(hechicera[asig_titulosh],adjetivos_fem[asig_adjectivosh])
  elif trabajo=='ARQUERA':
    print(arquera[asig_titulosh],adjetivos_fem[asig_adjectivosh])
  else:
    print("eri femboy?")

else:
  print("No digas mamadas meri yein")
