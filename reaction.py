from gpiozero import LED,Button
from time import sleep,time
from random import uniform
import sys
from signal import pause

led=LED(4)
right_button=Button(15)
left_button=Button(14)

left_name=input('left player name is:')
right_name=input('right player name is:')

start_time=0

reaction_time=time()-start_time
def pressed(button):
	if button.pin.number==14:
		print(f"{left_name}pressed in{reaction_time:.3f}seconds and won the game")
	else:
		print(f"{right_name}pressed in{reaction_time:.3f}seconds and won the game")
	sys.exit()

right_button.when_pressed=pressed
left_button.when_pressed=pressed

print("Get ready...")
led.on()
sleep(uniform(5,10))
led.off()

start_time=time()
print("GO!")

pause()
