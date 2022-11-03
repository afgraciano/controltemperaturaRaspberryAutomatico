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