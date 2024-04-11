from PBXMUSIC.core.bot import PBX
from PBXMUSIC.core.dir import dirr
from PBXMUSIC.core.git import git
from PBXMUSIC.core.userbot import Userbot
from PBXMUSIC.misc import dbb, heroku
from telethon import TelegramClient
from config import API_ID, API_HASH

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = PBX()
api = SafoneAPI()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

telethn = TelegramClient("PBXMUSIC", API_ID, API_HASH)
