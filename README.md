YouTube to MP3 Telegram Bot
This is a simple Telegram bot that allows users to convert YouTube videos into MP3 audio files. Just send the YouTube video URL, and the bot will respond with a download link for the MP3 file.

Features
Convert YouTube video links to MP3 format.
User-friendly interface with inline buttons for navigation.
Fast processing and immediate MP3 file download.
No third-party software required.
Installation
Prerequisites
Python 3.7+.
Install required Python libraries by running:
bash
Копіювати код
pip install yt-dlp python-telegram-bot
Setting Up
Clone this repository:

bash
git clone https://github.com/decodeigor/youtube-to-mp3-bot.git
cd youtube-to-mp3-bot
Create a new bot on Telegram and get the API token by chatting with BotFather.

Replace the TOKEN variable in bot.py with your bot’s API token:

python
TOKEN = 'your-telegram-bot-token'
Run the bot:

bash
python bot.py
The bot should now be running, and you can start sending YouTube links to get MP3 files!

How to Use
Start the bot by clicking the "Start" button.
Send a YouTube video link.
Wait for the bot to process the video and send the MP3 file.
Download the MP3 and enjoy your music!
Bot Commands
/start – Start the bot and show the main menu.
Send any YouTube video link – Convert the video to MP3.
Links
Telegram
GitHub Repository
Author
Created by @igoraa001.

License
This project is licensed under the MIT License - see the LICENSE file for details.

