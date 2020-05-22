"""
Comandi:
.sega"""


from telethon import events

from userbot.utils import admin_cmd

import asyncio



@borg.on(admin_cmd(pattern=f"fuck", allow_sudo=True))
@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "sega":

        await event.edit(input_str)

        animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "8===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])
