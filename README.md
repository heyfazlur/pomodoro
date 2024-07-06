# pomodoro
A simple tool that helps using the pomodoro technique with concentration music. 

# Pomodoro CLI with YouTube Audio

This application is a command-line interface (CLI) Pomodoro timer that integrates with YouTube to play audio during your Pomodoro sessions. It helps you manage your work sessions and breaks with the added benefit of listening to focus-enhancing music from YouTube.

## Features

- **Pomodoro Timer:** Uses the traditional Pomodoro technique with configurable times for work sessions, short breaks, and long breaks.
- **YouTube Audio Integration:** Plays audio from a specified YouTube video to enhance focus during work sessions.
- **Customizable Settings:** Allows users to configure work and break durations and select their preferred YouTube audio tracks.

## Getting Started

### Prerequisites

Before installing the application, ensure you have the following:
- Python 3.6 or higher
- pip (Python package installer)

### Installation

Follow these steps to get your development environment running:

1. **Clone the repository**

git clone https://github.com/heyfazlur/pomodoro/
cd pomodoro-cli



2. **Set up a virtual environment** (Optional but recommended)
- For Windows:
  ```
  python -m venv env
  env\Scripts\activate
  ```
- For macOS and Linux:
  ```
  python3 -m venv env
  source env/bin/activate
  ```

3. **Install the required packages**
pip install -r requirements.txt


### Configuration

Modify the `config.ini` file to set your desired session lengths and specify the YouTube URL for background music:

```ini
[Settings]
youtube_url = https://www.youtube.com/watch?v=example_url
work_time = 25  # Duration of work sessions in minutes
short_break = 5  # Duration of short breaks in minutes
long_break = 15  # Duration of long breaks in minutes
