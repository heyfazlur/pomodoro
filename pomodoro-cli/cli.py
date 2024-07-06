# Filename: cli.py

import click
from pomodoro_timer import PomodoroTimer
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

@click.group()
def cli():
    pass

@cli.command()
@click.option('--youtube_url', prompt='Enter YouTube URL for focus music', help='YouTube video URL for background music.')
def start(youtube_url):
    youtube_url = youtube_url if youtube_url else config.get('Settings', 'youtube_url', fallback='default_url')
    timer = PomodoroTimer(youtube_url=youtube_url)
    timer.start()

@cli.command()
def pause():
    # Note: You'll need to maintain the state of the timer instance across commands, or refactor to support shared state.
    pass

@cli.command()
def stop():
    # Similar to the pause command, manage shared state appropriately.
    pass

if __name__ == "__main__":
    cli()
