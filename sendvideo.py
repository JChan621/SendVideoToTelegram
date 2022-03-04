# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 18:12:18 2022

@author: TZEHIM
"""

from telethon.tl.types import DocumentAttributeVideo
import asyncio
from telethon import TelegramClient
import os
PATH = r'C:\Users\TZEHIM\Documents\GitHub\video-splitter'
api_id = 1314345
api_hash = 'b60041bdda5f4ca6a3073c960959a61e'
bot_token = '1147505946:AAH48sNZfzrf1QBoymNks9tCQs4RHQHj1y4'
client = TelegramClient('C:/Users/TZEHIM/Downloads/session/', api_id, api_hash)
client.start(phone = '85222683201',password = 'TakagiReni621')
files = os.listdir(PATH)
print(files)
async def prog():
    for file in files:
        if file.startswith('testx'):
            await client.send_file('me', os.path.join(PATH, file), attributes = (DocumentAttributeVideo(0, 0, 0),))

with client:
    client.loop.run_until_complete(prog())
