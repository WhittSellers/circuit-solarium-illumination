from typing import NamedTuple, List
# me - this DAT
#
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
#
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

"""This is for controlling clips via TouchDesigner.  Here is the docs for the AbletonClipSlot Op

abletonClipSlot
Provides access to Tracks' clip slots. Select a Track on the Ableton Track parameter page, then a clip slot on the Ableton Clip Slot page. This component provides callbacks when clips are triggered and playing.

Extra outputs: clips is a table of clip information for the track, including source files. clip_status is a table showing triggered and playing clips. When a midi clip slot is selected, the midiClip output gives a list of midi notes in the range named in the MIDI Clip Time Range and MIDI Clip Note Range parameters.

Clip Functions
The abletonClipSlot Component provides these functions for working with clips:

SetNotes(notes)

Send a set notes command to the chosen clip.
notes: a tuple of tuples in the form (pitch, time, duration, velocity, mute)
pitch: MIDI (0-127 int)
time: Beat (0-4 float)
duration: in beats
velocity: MIDI (0-127 int)
mute: 1 to mute, 0 to play
RemoveNotes(timeStart, pitchStart, timeEnd, pitchEnd)

Remove all notes that start in the given range. Time is in beats, pitch is in midi values (0-127)
timeStart: Beat (0-4 float)
pitchStart: MIDI (0-127 int)
timeEnd: number of beats from timeStart to end of removal area (0-4 float)
pitchEnd: number of notes from pitchStart to bottom of removal area (0-127 int)
ClipCommand(command)

Send this command to the selected clip.
command: a string to be sent to the Live clip object in the form <clip object>.<command>
For a list of clip commands, search for "Clip.Clip" at:
http://julienbayle.net/PythonLiveAPI_documentation/Live9.6.xml
"""

def makeNote(row: List):
	"""Specifically a list of td.Cells"""
	pitch = int(row[0].val)
	time = float(row[1].val)
	duration = float(row[2].val)
	velocity = int(row[3].val)
	mute = row[4].val != '0'
	return Note(pitch, time, duration, velocity, mute)

class Note(NamedTuple):
	pitch: int
	time: float
	duration: float
	velocity: int
	mute: bool

class Clip:
	def __init__(self, clipOp: str):
		self.clipOp = clipOp
		self.clipOp.par.Midiclipoutput = '1'
		clip = op(self.clipOp.outputs[3])
		rows = clip.rows(*range(1, clip.numRows))
		self.notes = [makeNote(row) for row in rows]

    writeClip(self):
        self.clipOp.SetNotes()


def onOffToOn(channel, sampleIndex, val, prev):

	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	return
