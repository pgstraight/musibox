#!/usr/bin/python

import time
import rtmidi

midiin = rtmidi.MidiIn()
midiout = rtmidi.MidiOut()

print midiin.get_ports()
print midiout.get_ports()

midiin.open_port(1)
midiout.open_port(2)


try:
    timer = time.time()
    while True:
        msg = midiin.get_message()

        if msg:
            message, deltatime = msg
            timer += deltatime
            print("@%0.6f %r" % (timer, message))

            type = message[0]
            note = message[1]
            vol = message[2]

            midiout.send_message(message)


        #time.sleep(0.01)
except KeyboardInterrupt:
    print('')
finally:
    print("Exit.")
    midiin.close_port()
    del midiin

















#ports = midiout.get_ports()
#print ports



#a = rtmidi.midiutil.list_available_ports()
