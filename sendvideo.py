# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 18:12:18 2022

@author: Fourier
"""

from telethon.tl.types import DocumentAttributeVideo
import asyncio
from telethon import TelegramClient
import os
PATH = 'your folder dir'
api_id = 'your api id'
api_hash = 'your api hash'
#bot_token = 'your bot token' #Not used
client = TelegramClient('your telegram session dir', api_id, api_hash)
client.start(phone = 'your phone',password = 'your password')
files = os.listdir(PATH)
print(files)
async def prog():
    for file in files:
        if file.startswith('testx'): #A list of videos created and named with testx##3.mov.
            await client.send_file('me', os.path.join(PATH, file), attributes = (DocumentAttributeVideo(0, 0, 0),))

with client:
    client.loop.run_until_complete(prog())
