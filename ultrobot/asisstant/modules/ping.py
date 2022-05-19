from datetime import datetime
from telethon import events
from ultrobot import OWNER_ID
from ultrobot.asisstant.events import ultro
import asyncio

@ultro(incoming=True, from_users=OWNER_ID, pattern="^/ping")
async def evnt (e):
    start = datetime.now()
    msg = await e.reply("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"**Pong!!**\n `{ms} ms`")
    
    

