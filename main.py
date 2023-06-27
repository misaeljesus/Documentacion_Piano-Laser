from picozero import Speaker
from time import sleep
from machine import Pin
# from picodfplayer import DFPlayer
altavoz_1=Speaker(13)
sensor_1=Pin(16, Pin.IN)
sensor_2=Pin(17, Pin.IN)
sensor_3=Pin(18, Pin.IN)
sensor_4=Pin(19, Pin.IN)
sensor_5=Pin(20, Pin.IN)
sensor_6=Pin(21, Pin.IN)
sensor_7=Pin(22, Pin.IN)
sensor_8=Pin(26, Pin.IN)
# boton_1=Pin(28, Pin.IN)
# boton_2=Pin(27, Pin.IN)
# UART_INSTANCE=0
# TX_PIN=17
# RX_PIN=18 
# BUSY_PIN=6
# player=DFPlayer(UART_INSTANCE, TX_PIN, RX_PIN, BUSY_PIN)
# led_3=Pin(1,Pin.OUT)
# led_2=Pin(2,Pin.OUT)
led_1=Pin(3,Pin.OUT)
# playing=False

while True:
    if sensor_1.value() == 1:
        altavoz_1.play("c3",0.1)
        led_1.value(1)
    elif sensor_2.value() == 1:
        altavoz_1.play("d3",0.1)
        led_1.value(1) 
    elif sensor_3.value() == 1:
        altavoz_1.play("e3",0.1)
        led_1.value(1)
    elif sensor_4.value() == 1:
        altavoz_1.play("f3",0.1)
        led_1.value(1)
    elif sensor_5.value() == 1:
        altavoz_1.play("g3",0.1)
        led_1.value(1)
    elif sensor_6.value() == 1:
        altavoz_1.play("a3",0.1)
        led_1.value(1)
    elif sensor_7.value() == 1:
        altavoz_1.play("b3",0.1)
        led_1.value(1)
    elif sensor_8.value() == 1:
        altavoz_1.play("c4",0.1)
        led_1.value(1)         
    else:
        led_1.value(0)
  