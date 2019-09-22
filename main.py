import pyb
#import Pin so we can use it in the project
from pyb import Pin
from pyb import Switch

#set p_out to Pin X1
p_out = Pin('X1', Pin.OUT_PP)

#just a variable so the loop never stops
x=0
#while loop to continually blink the led in Pin X1

sw = Switch()
#when user switch is pressed the LED toggles on or off
sw.callback(lambda: pyb.LED(3).toggle())

while x==0:
     p_out.high()
     pyb.delay(500)
     p_out.low()
     pyb.delay(500)
