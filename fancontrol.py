#!/usr/bin/env python3

import time
import psutil #libreria para saber la carga del procesador
import multiprocessing #libreria usada para saber cuantos nucleos hay de procesador

from gpiozero import OutputDevice

ON_THRESHOLD = 65  # (degrees Celsius) Fan kicks on at this temperature.
OFF_THRESHOLD = 55  # (degress Celsius) Fan shuts off at this temperature.
SLEEP_INTERVAL = 2  # (seconds) How often we check the core temperature.
GPIO_PIN = 17  # Which GPIO pin you're using to control the fan.

def get_temp():
    """Get the core temperature.

    Read file from /sys to get CPU temp in temp in C *1000

    Returns:
        int: The core temperature in thousanths of degrees Celsius.
    """
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        temp_str = f.read()

    try:
        return int(temp_str) / 1000
    except (IndexError, ValueError,) as e:
        raise RuntimeError('Could not parse temperature output.') from e

if __name__ == '__main__':
    # Validate the on and off thresholds
    if OFF_THRESHOLD >= ON_THRESHOLD:
        raise RuntimeError('OFF_THRESHOLD must be less than ON_THRESHOLD')

    fan = OutputDevice(GPIO_PIN)

    while True:
          
        temp = get_temp()
        #las variables que van cambiando usadas y para mostrarlas en las pruebas 
        #cpu = int(psutil.cpu_percent(interval=0.1))
        cpuunocincoquince = str(psutil.getloadavg()) #porcentaje carga cpu 1 min 5 min 15 min en string
        usocpu=(psutil.getloadavg()) # valores de promedio de carga de cpu en 1 5 15 min en flotante
        usocpu1=usocpu[0] #optencion valor carga cpu en 1 min
        #usocpu2=usocpu[1] #optencion valor carga cpu en 5 min
        nucleos=multiprocessing.cpu_count()#metodo devuelte numero de nucleos del cpu
        pcpu=(100*usocpu1)/nucleos #formula para saber porcentaje de uso de la cpu cada 1 min
        #pcpu1=(100*usocpu2)/nucleos #formula para saber porcentaje de uso de la cpu cada 5 min

        # Start the fan if the temperature has reached the limit and the fan
        # isn't already running.
        # NOTE: `fan.value` returns 1 for "on" and 0 for "off"
        if ((temp > ON_THRESHOLD) or (pcpu > 50 )) and not fan.value:
            fan.on() #activacion del pin GPIO17
            #print("INICIO VENTILADOR")
       
        # Stop the fan if the fan is running and the temperature has dropped
        # to 10 degrees below the limit.
        elif fan.value and ((temp < OFF_THRESHOLD)and(pcpu < 50)):
            fan.off() #desactivacion del pin GPIO17
            #print("APAGADO VENTILADOR")
        
	#variables que se van mostrando en las pruebas

        #print("CPU Info–> ", repr (cpu) + "%")
        #print("TEMPERATURA Info–> ", repr (temp) +" Grados")
        #print("CPUunocincoquince Info–> ", (cpuunocincoquince) + "promedio carga cpu 1min 5min 15min")
        #print("CPU Info por minuto–> ", (usocpu1[1]+usocpu1[2]+usocpu1[3]+usocpu1[4]) + "%")
        #print("CPU Info por minuto promedio carga–> ", (usocpu1))
        #print("CPU Info por minuto porcentaje–> ", repr (pcpu) + "%")
        #print("CPU Info por 5minutos promedio carga–> ", (usocpu2))
        #print("CPU Info por 5minutos porcentaje–> ", repr (pcpu1) + "%")
        #print("numero de nucleos del cpu–> ", (nucleos))
        #print("\n")#espacio para separar la informacion cada segundo

        time.sleep(SLEEP_INTERVAL)
