# Pi controlar ventilador

Raspberry Pi controlador ventilador.

## Description

Este repositorio proporciona scripts que se pueden ejecutar en Raspberry Pi y que
controle la temperatura central y encienda el ventilador cuando la temperatura alcance
cierto rango, o cuando la carga de procesador sea alta aunque no este con alta temperatura;
y que apague el ventilador cuando este bajo los 55 grados de temperatura y el porcentaje
de carga que uno asigne


Para usar este código, tendrás que instalar un ventilador conectado a un transistor NPN 2N2222 (emisor
al pin neutro del ventilador y colector al polo tierra de la raspberry) y una resistencia de 680 Ω 
hacia el pin base del transistor, y el pin de voltaje positivo del ventilador al pin fuente de 
la raspberry de 5 voltios. 

tenemos 3 archivos, uno es el script para que se ejecute automaticamente el programa al iniciar la 
raspberry llamado fancontrol.sh, el fancontrol.py es el programa ejecutable automaticamente, y 
tenemos un tercer archivo llamado fancontrol_valoresDePrueba.py que sirve para hacer algunas pruebas 
por consola mostrando resultados cada 2 segundos de los valores que se requieren.

para cargar los archivos en la raspberry para que quede de forma automatica, se ejecutan 
los siguientes comandos en terminal desde la carpeta donde tenemos los archivos descargados:

sudo mv fancontrol.py /usr/local/bin/
sudo chmod +x /usr/loca/bin/fancontrol.py
sudo mv fancontrol.sh /etc/init.d/
sudo chmod +x /etc/init.d/fancontrol.sh
sudo update-rc.d fancontrol.sh defaults
sudo /etc/init.d/fancontrol.sh start

estos comandos cargan los archivos a las carpetas donde se van a ejecutar de forma automatica y 
los hace ejecutables ademas de registrar el script para que se ejecute al arranque del sistema.