import re

instruments = {
	'ST': 31,
	'BS': 35,
	'SD': 37,
	'S1': 38,
	'S2': 40,
	'HC': 42,
	'HO': 46,
	'HH': 44,
	'CR': 49,
	'TR': 51,
	'T1': 47,
	'T2': 48,
	'T3': 50
}

globalPlayer = 0

def playDrum(instrument, volume = 8):
	ins = 0;
	if isinstance(instrument, basestring):
		if instrument in instruments:
			ins = instruments[instrument]
	else:
		ins = instrument
	Drums.player.note_on(ins, (volume+1)*12, 9)


class Drums(object):
	player = 0
	
	def __init__(self, player):
		self.player = player
		self.beats = {}
		self.currentBeat = 0
		self.currentSequence = 0

	def beat(self, instrument, volume = 8):
		ins = 0;
		if isinstance(instrument, basestring):
			if instrument in instruments:
				ins = instruments[instrument]
		else:
			ins = instrument
		self.player.note_on(ins, (volume+1)*12, 9)

	def loadBeat(self, name):
		if name not in self.beats:
			self.beats[name] = Beat(name)

	def setBeat(self, name):
		self.loadBeat(name)
		self.currentSequence = 0
		self.currentBeat = self.beats[name]
		self.currentBeat.start()

	def idle(self):
		beat = self.currentBeat
		if beat:
			beat.idle(self.player)
			
		
		
		
class Beat(object):

	def __init__(self, name):
		self.length = 0
		self.tracks = []
		self.load(name)
		self.pos = 0;
	
	def load(self, name):
		lines = self.loadFile(name)
		for line in lines:
			track = Track(line)
			if (track.length > 0):
				if (track.length > self.length):
					self.length = track.length
				self.tracks.append(track)
	
	def loadFile(self, name):
		fname = './beats/' + name + '.beat'
		f = open(fname)
		lines = f.readlines()
		f.close()
		return lines
		
	def start(self):
		self.pos = 0;
	
	def idle(self, player):
		if self.pos >= self.length:
			self.pos = 0
		for track in self.tracks:
			track.play(self.pos, player)
		self.pos += 1
		
class Track(object):
	def __init__(self, line):
		self.length = 0
		self.instrument = 0
		self.notes = []
		res = re.search(r'^(.+):(.+)$', line)
		if (res):
			ins = res.group(1)
			if ins in instruments:
				tab = res.group(2)
				self.length = len(tab)
				self.instrument = instruments[ins]
				for i in range(self.length):
					inote = 0
					snote = tab[i:i+1]
					if (re.search(r'^\d$', snote)): inote = int(snote)
					self.notes.append(inote)

	def play(self, pos, player):
		#print self.notes
		self.player = player
		if pos < self.length:
			volume = self.notes[pos]
			#print pos,self.instrument, volume
			if volume > 0:
				self.beat(self.instrument, volume)
				#print globalPlayer
				#playDrum(self.instrument, volume)
				#print self.instrument, volume

	def beat(self, instrument, volume = 8):
		ins = 0;
		if isinstance(instrument, basestring):
			if instrument in instruments:
				ins = instruments[instrument]
		else:
			ins = instrument
		self.player.note_on(ins, (volume+1)*12, 9)
