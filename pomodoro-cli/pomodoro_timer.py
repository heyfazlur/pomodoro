# Filename: pomodoro_timer.py

import time
from pytube import YouTube
import vlc
from configparser import ConfigParser

class PomodoroTimer:
    def __init__(self, work_time=25, short_break=5, long_break=15, long_break_after=3, youtube_url=None):
        self.work_time = work_time * 60  # Convert minutes to seconds
        self.short_break = short_break * 60
        self.long_break = long_break * 60
        self.long_break_after = long_break_after
        self.cycles = 0
        self.running = False
        self.current_timer = None
        self.youtube_url = youtube_url
        self.player = None

    def setup_audio(self):
        yt = YouTube(self.youtube_url)
        audio_stream = yt.streams.get_audio_only()
        media = vlc.MediaPlayer(audio_stream.url)
        self.player = media

    def start_audio(self):
        if self.player is not None:
            self.player.play()

    def stop_audio(self):
        if self.player is not None:
            self.player.stop()

    def display_tree_progress(self, start_time, end_time):
        elapsed_time = time.time() - start_time
        total_time = end_time - start_time
        progress_percentage = (elapsed_time / total_time) * 100
        # Assuming the tree grows to 10 stages
        tree_size = int((progress_percentage / 100) * 10)
        tree_graphic = '🌲' * tree_size
        print(f"\r{tree_graphic} {progress_percentage:.2f}% Complete", end='')

    def start_timer(self, duration):
        self.running = True
        start_time = time.time()
        end_time = start_time + duration
        while time.time() < end_time and self.running:
            time.sleep(1)
            mins, secs = divmod(int(end_time - time.time()), 60)
            self.display_tree_progress(start_time, end_time)
            print(f" Time Left: {mins:02}:{secs:02}", end='')

    def start(self):
        self.setup_audio()
        self.start_audio()
        while self.cycles < self.long_break_after:
            print("\nWork time!")
            self.start_timer(self.work_time)
            self.cycles += 1
            if self.cycles % self.long_break_after == 0:
                print("\nLong break")
                self.start_ti
