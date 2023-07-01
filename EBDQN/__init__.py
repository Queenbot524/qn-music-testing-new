from aiohttp import ClientSession
from .console import LOGGER

from EBDQN.modules.core.app import App
from EBDQN.modules.core.bot import Bot
from EBDQN.modules.core.dirs import dirr
from EBDQN.modules.core.git import git
from EBDQN.misc import dbb, heroku, sudo

dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = App()

bot = Bot()


from EBDQN.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
