import asyncio
import importlib
from sys import argv
from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from PBXMUSIC import LOGGER, app, userbot
from PBXMUSIC.core.call import PBX
from PBXMUSIC.misc import sudo
from PBXMUSIC.plugins import ALL_MODULES
from PBXMUSIC.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS



async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "ᴀʙᴇ ʟᴏᴠᴅᴇ ʟᴏɢɢᴇʀ ɢʀᴏᴜᴘ ᴍᴇ ᴀᴅᴍɪɴ ᴛᴇʀᴀ ʙᴀᴘ ᴋʀᴇ ɢᴀ ᴋʏᴀ"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            if user_id not in BANNED_USERS:
                BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("PBXMUSIC.plugins" + all_module)
    LOGGER("PBXMUSIC.plugins").info("ꜱᴏ ꜱᴀᴅ 🥳...")

    await userbot.start()

    await PBX.start()
    await PBX.decorators()
    await restart_bots()
    LOGGER("PBXMUSIC").info("╔═════ஜ۩۞۩ஜ════╗\n  ♨️ᴍᴀᴅᴇ ʙʏ ᴛᴇᴀᴍ ᴘʙx ♨️\n╚═════ஜ۩۞۩ஜ════╝")
    await idle()

    await app.stop()
    await userbot.stop()

    LOGGER("PBXMUSIC").info(
        "                 ╔═════ஜ۩۞۩ஜ════╗\n  ♨️ᴍᴀᴅᴇ ʙʏ ᴛᴇᴀᴍ ᴘʙx ♨️\n╚═════ஜ۩۞۩ஜ════╝"
    )


if __name__ == "__main__":

    asyncio.get_event_loop().run_until_complete(init())
