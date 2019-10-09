#!/usr/bin/python
import re
import pygame
import pygame.midi
from Drums import Drums



def print_device_info():
	pygame.midi.init()
	_print_device_info()
	pygame.midi.quit()

def _print_device_info():
	for i in range( pygame.midi.get_count() ):
		r = pygame.midi.get_device_info(i)
		(interf, name, input, output, opened) = r
		in_out = ""
		if input:
			in_out = "(input)"
		if output:
			in_out = "(output)"

		print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
			(i, interf, name, opened, in_out))






pygame.init()
pygame.display.set_mode((800, 600))
pygame.midi.init()
pygame.event.set_grab(0)


#_print_device_info()
#exit()



player = pygame.midi.Output(4)
midin = pygame.midi.Input(3)
instrument = 0;


drums = Drums(player)
drums.setBeat('14')


tempo = 120
ticker1 = pygame.time.get_ticks()

player.set_instrument(instrument)
while 1:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		exit()
	if event.type == pygame.KEYDOWN:
		if event.key == 27:
			exit()
	if midin.poll():
		midi_events = midin.read(10)
		for midi_event in midi_events:
			p = midi_event[0][0]
			note = midi_event[0][1]
			vel = midi_event[0][2]
			if p == 144:
				player.note_on(note, vel, 0)
			if p == 128:
				player.note_off(note, vel, 0)
	msdelay = 15000 / tempo
	ticker2 = pygame.time.get_ticks()

	if ticker2 - ticker1 > msdelay:
		ticker1 = ticker2
		drums.idle()
		





#drums.beat('S1')


exit()



#player.set_instrument(instrument)


#print pygame.midi.get_count()


#print pygame.KEYDOWN


DR_STICKS = 31
DR_BASS = 35
DR_SIDE = 37
DR_SNARE1 = 38
DR_SNARE2 = 40
DR_HAT = 42
DR_HATHAT = 44
DR_OPENHAT = 46
DR_CRASH = 49
DR_TAR = 51
DR_TOM1 = 47
DR_TOM2 = 48
DR_TOM3 = 50








kbnotes = {113:64, 97:65, 122:66, 119:67,115:68,120:69,101:70,100:71,99:72,114:73,102:74,118:75,116:76,103:77,98:78,121:79,104:80,110:81,117:82,106:83,109:84,105:85,107:86,44:87,111:88,108:89,46:90,112:91,59:92,47:93}




while 1:
	event = pygame.event.poll()
	if event.type == pygame.QUIT:
		exit()
	if event.type == pygame.KEYDOWN:
		if event.key == 27:
			exit()
		print event.key

#	if event.type == pygame.KEYDOWN and event.key == 32:
#		player.note_on(64, 127)
#		print "+"
#	if event.type == pygame.KEYUP and event.key == 32:
#		player.note_off(64, 127)
#		print "-"
	
	if event.type == pygame.KEYDOWN and event.key in kbnotes:
		player.note_on(kbnotes[event.key], 127, 9)
	
	if event.type == pygame.KEYUP and event.key in kbnotes:
		player.note_off(kbnotes[event.key], 127, 9)
	
	if event.type == pygame.KEYDOWN:
		if event.key == 282:
			player.note_on(DR_HAT, 127, 9)
		if event.key == 283:
			player.note_on(DR_OPENHAT, 127, 9)
		if event.key == 284:
			player.note_on(DR_BASS, 127, 9)
		if event.key == 285:
			player.note_on(DR_SNARE1, 127, 9)
		if event.key == 286:
			player.note_on(DR_SNARE2, 127, 9)
			
		if event.key == 275:
			instrument += 1;
			#player.set_instrument(instrument)
			#player.note_on(instrument, 127, 9)
			print '=',instrument
	
	if event.type == pygame.KEYUP:
		if event.key == 276:
			instrument -= 1;
			#player.set_instrument(instrument)
			#player.note_on(instrument, 127, 9)
			print '=',instrument
