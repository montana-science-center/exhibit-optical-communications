#!/bin/python

import subprocess

from gpiozero import Button
from signal import pause

WAV_FILE = '/home/msc/recording.wav'

class Recorder:

    def start(self):
        self.proc = subprocess.Popen(['arecord', '--device=plughw:CARD=Device,DEV=0', '--channels=1',
            '--format=S16_LE', '--rate=44100', WAV_FILE])

    def stop(self):
        self.proc.terminate()

def playback():
    subprocess.run(['aplay', '--device=plughw:CARD=Device,DEV=0', WAV_FILE])


def main():

    recorder = Recorder()

    record_button = Button(26, bounce_time=None)
    record_button.when_pressed = recorder.start
    record_button.when_released = recorder.stop

    play_button = Button(16,bounce_time=None)
    play_button.when_pressed = playback

    pause()


if __name__ == "__main__":
    main()
