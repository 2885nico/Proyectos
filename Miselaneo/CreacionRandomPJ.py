import random

guerrero = ["Martillo", "Fuego", "Escudo", "Valor"]
guerrera = ["Espada", "Sangre", "Gloria", "Lucha"]

hechicero = ["Hechizo", "Saber", "Encantamiento", "Rayo"]
hechicera = ["Vara", "Magia", "Sabiduría", "Energía", "Esencia"]

arquero = ["Arco", "Viento", "Disparo", "Sombrío", "Sigilo"]
arquera = ["Flecha", "Precisión", "Sombra", "Destreza", "Puntería", "Centella", "Saeta"]

adjetivos_fem = ["Divertida", "Chiflada", "Bromista", "Despistada", "Risueña", "Alocada", "Traviesa", "Payasa", "Juguetona", "Tronchante"]

adjetivos_masc = ["Divertido", "Chiflado", "Bromista", "Despistado", "Risueño", "Alocado", "Travieso", "Payaso", "Juguetón","Tronchante"]

sexo=['Masculino','Femenino']
trabajo_masc=['Guerrero','Hechicero','Arquero']
trabajo_fem=['Guerrera','Hechicera','Arquera']

asig_sexo=random.randint(0,1)
asig_trabajo=random.randint(0,2)
asig_titulo=random.randint(0,3)
asig_cualidad=random.randint(0,9)

print(sexo[asig_sexo])

if asig_sexo==0:
  print(trabajo_masc[asig_trabajo])
  if asig_trabajo==0:
    print(guerrero[asig_titulo],adjetivos_masc[asig_cualidad])
  elif asig_trabajo==1:
    print(hechicero[asig_titulo],adjetivos_masc[asig_cualidad])
  else:
    print(arquero[asig_titulo],adjetivos_masc[asig_cualidad])
else:
  print(trabajo_fem[asig_trabajo])
  if asig_trabajo==0:
    print(guerrera[asig_titulo],adjetivos_fem[asig_cualidad])
  elif asig_trabajo==1:
    print(hechicera[asig_titulo],adjetivos_fem[asig_cualidad])
  else:
    print(arquera[asig_titulo],adjetivos_fem[asig_cualidad])
