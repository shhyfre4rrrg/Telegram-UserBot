# This is a troll indeed ffs *facepalm*
import asyncio
from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import ChannelParticipantsAdmins
from userbot.utils import admin_cmd


@borg.on(admin_cmd("gbun"))
async def gbun(event):
    if event.fwd_from:
        return
    gbunVar = event.text
    gbunVar = gbunVar[6:]
    mentions = "Attenzione!! Utente **BANNATO** da un Admin!...\n`"
    no_reason = "__Motivo: Non definito. __"
    await event.edit("**Hackerando il bot di Sicurezza... ❗️⚜️☠️**")
    asyncio.sleep(3.5)
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        # make meself invulnerable cuz why not xD
        if idd == 304506948:
            await reply_message.reply("`Aspetta un attimo... Bastardo questo è il mio Boss!`\n**Come cazzo ti permetti strunz?!**\n\n__Il tuo acocount è stato bloccato! Dai 30€ ad __ [AnonHexo](t.me/AnonHexo) __ per sbloccarti__😏")
        else:
            jnl=("`Warning!! `"
                  "[{}](tg://user?id={})"
                  " 𝙂𝘽𝘼𝙉𝙉𝙀𝘿 da un Admin...\n\n"
                  "**Nome del nubbo: ** __{}__\n"
                  "**ID : ** `{}`\n"
                ).format(firstname, idd, firstname, idd)
            if usname == None:
                jnl += "**Nubbo: ** non è neanche degno di un username -.-\n"
            elif usname != "None":
                jnl += "**nubbo** : @{}\n".format(usname)
            if len(gbunVar) > 0:
                gbunm = "`{}`".format(gbunVar)
                gbunr = "**Reason: **"+gbunm
                jnl += gbunr
            else:
                jnl += no_reason
            await reply_message.reply(jnl)
    else:
        mention = "Attenzione!! User **BANNATO** da un Admin...\nMotivo: Non definito. "
        await event.reply(mention)
    await event.delete()
