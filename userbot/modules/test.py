from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
from covid import Covid
import time
from collections import deque
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import sys
import json
from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
import requests
from cowpy import cow
from userbot import CMD_HELP
from userbot.events import javes05
from userbot.modules.group import get_user_from_event
from telethon import events
import asyncio
from datetime import datetime
import requests
import json
from telethon import events
import asyncio



@javes05(outgoing=True, pattern="^!calander(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    input_str = event.pattern_match.group(1)
    input_sgra = input_str.split("-")
    if len(input_sgra) == 3:
        yyyy = input_sgra[0]
        mm = input_sgra[1]
        dd = input_sgra[2]
        required_url = "https://calendar.kollavarsham.org/api/years/{}/months/{}/days/{}?lang={}".format(yyyy, mm, dd, "en")
        headers = {"Accept": "application/json"}
        response_content = requests.get(required_url, headers=headers).json()
        a = ""
        if "error" not in response_content:
            current_date_detail_arraays = response_content["months"][0]["days"][0]
            a = json.dumps(current_date_detail_arraays, sort_keys=True, indent=4)
        else:
            a = response_content["error"]
        await event.edit(str(a))
    else:
        await event.edit("SYNTAX: .calendar YYYY-MM-DD")
    end = datetime.now()
    ms = (end - start).seconds

@javes05(outgoing=True, pattern="^!call(?: |$)(.*)")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 18)

   # input_str = event.pattern_match.group(1)

   # if input_str == "call":

    await event.edit("Calling")

    animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` @javes05 ,`Please Connect me to my lil bro,lel`",
            "`User Authorised.`",
            "`Calling lel Durov`  `At +916969696969`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`lel: May I Know Who Is This?`",
            "`Me: Yo Brah, I Am` @javes05 ",
            "`lel: OMG!!! Long time no see, Wassup Brother...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Brah.`",
            "`lel: Please Don't Thank Brah, Telegram Is Our's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`lel: Yes Sur, There Is A Bug In Telegram v69.6.9.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`lel: Sure Sur \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 18])




