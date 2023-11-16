# DFPlayer
ESP32 Micropython DFPlayer
Original Library from another GITHUB repository, will add credit when I find it again - thanks

Just download 2 files main.py and dfplayer.py and send them to the ESP32 with Thonny

Connections are written in main.py Just +5v GND RX and TX. Connect a Speaker and you're ready.

Added to original library:

RANDOM function to allow easy playing and testing. Works without renaming tracks.

Got the is_playing() function to work so you can detect the end of the tracks.

Added timeout feature to 'send_query()' function and catch errors.
