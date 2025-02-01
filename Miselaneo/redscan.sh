#!/bin/bash
ifconfig | grep inet| sed 's/^[[:space:]]*//' > miip.txt;
ip=$(cut -d " " -f 2 miip.txt | sed -n '1p'| cut -d "." -f 1-3); miip=$(cut -d " " -f 2 miip.txt | sed -n '1p');echo "mi ip es:" ${miip};echo "calculando...";
#254
for i in {1..254}; do(ping -c 1 ${ip}.${i});   done 2>/dev/null |  grep "bytes from" > ips.txt;
echo "las ip vecinas son: ";
cut -d " " -f 4 ips.txt | sed 's/.$//'| sort | uniq > ipslimpias.txt;
cat ipslimpias.txt;
#65535
while IFS= read -r ip; do
   for port in 1..65535}; do
     echo > /dev/tcp/$ip/$port && echo "$port abierto en la ip $ip" > ipsescaneadas.txt
     done
done < ipslimpias.txt 2>/dev/null
