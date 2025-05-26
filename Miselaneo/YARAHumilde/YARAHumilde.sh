#!/bin/bash

figlet "YARAHumilde"
echo "By: 2885"
echo "- Procura usar con cuidado el bash, ta chikito"
echo "- Se requiere experiencia previa creando reglas YARA, como dije esta chikito, y puede tener errores, asi que paciencia"
echo "- No me basureen el ejecutable oye, todo con buenas intenciones"
echo "- Las modificaciones a tu regla se las puedes hacer con nano y asi"
echo "- Ojala te facilite la pega, muak :*"


echo -e "Asigna un nombre a tu regla YARA: "
read nombreYARA

echo -e "Asigna una descripcion para tu regla YARA: "
read descripcionYARA

echo -e "Escribe el nombre del creador de esta regla YARA"
read creadorYARA

echo -e "Escribe alguna indicacion para esta regla YARA"
read disclaimerYARA

#crear y llenar el archivo

archivo=$nombreYARA.yara
touch $archivo

echo "rule $nombreYARA" >> $archivo
echo "{" >> $archivo
echo "  meta:" >> $archivo
echo "          author = $creadorYARA" >> $archivo
echo "          disclaimer = $disclaimerYARA" >> $archivo
echo "          description = $descripcionYARA" >> $archivo

echo "  strings:" >> $archivo

while true; do
        echo -e "ingresa tu regla: "
        read reglaYARA
        echo "          $ = $reglaYARA" >> $archivo
        echo -e "Quieres agregar otra regla?, si no ingresa 'no': "
        read opcion
        echo "eleccion seleccionada: $opcion"
        if [ "$opcion" = "no" ]; then
                echo "has elegido que no ingresaras mas reglas"
                break
                return false
        fi
done

echo "  condition: " >> $archivo
echo -e "agrega la condicion de aplicabilidad para esta regla YARA: "
read condicionYARA
echo "          $condicionYARA"  >> $archivo
echo "}" >> $archivo
