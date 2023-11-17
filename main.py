import time
from dfplayer import DFPlayer

# esp32       dfplayer
#  +5V          +5V
#  GND          GND
#  17  --1K--   RX
#  16           TX

df=DFPlayer(uart_id=1,tx_pin_id=17,rx_pin_id=16)

df.stop() # stop playing
df.volume(10) # 1-30
df.equal(5)  # set equaliser  0:Normal/1:Pop/2:Rock/3:Jazz/4:Classic/5:Bass

print("Volume ",df.get_volume())
print("EQ ",df.get_equal())
print("Waiting 5 seconds to allow break without music...")
time.sleep(5)

#df.random()  #track names can be left unchanged
# end program here, player will continue

df.play(3,1) #must name folders 01...02...03 and tracks 001.mp3...002.mpg...003.mpg
while df.is_playing() == True:
    pass  # wait for track to finish

df.play(2,1)
while df.is_playing() == True:
    pass

df.play(1,1)
while df.is_playing() == True:
    pass
