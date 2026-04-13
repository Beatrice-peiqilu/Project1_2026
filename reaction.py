from gpiozero import LED, Button
from time import sleep
from random import uniform
led = LED(4)
left_button = Button(14)
right_button = Button(15)
left_name = input("left player name is：")
right_name = input("right player name is：")

led.on()
sleep(uniform(5, 10))
led.off()


def pressed(button):
    if button.pin.number == 14:
      print(f"\n{left_name} 获胜！")
    else:
      print(f"\n{right_name} 获胜！")
    exit()
left_button.when_pressed = pressed
right_button.when_pressed = pressed
while True:
    sleep(1)
