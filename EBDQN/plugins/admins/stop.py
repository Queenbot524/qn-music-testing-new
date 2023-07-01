from pyrogram import filters
from pyrogram.types import Message

from EBDQN.utilities.config import BANNED_USERS
from EBDQN.utilities.strings import get_command
from EBDQN import bot
from EBDQN.modules.core.call import Kaal
from EBDQN.modules.main.database import set_loop
from EBDQN.modules.main.decorators import AdminRightsCheck
from EBDQN.utilities.events.filters import command
from EBDQN.utilities.inline.play import close_keyboard

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")


@bot.on_message(
    command(STOP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@AdminRightsCheck
async def stop_music(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    await Kaal.stop_stream(chat_id)
    await set_loop(chat_id, 0)
    await message.reply_text(
        _["admin_9"].format(message.from_user.first_name),
        reply_markup=close_keyboard,
    )
