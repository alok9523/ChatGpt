import asyncio
import os
import random
import sys
from datetime import datetime

import telethon.utils
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

from Config import (
    API_HASH,
    API_ID,
    STRING,
)
from Utils import RAID, RRAID

grp = os.environ.get("GROUP_USERNAME", None) or "LB_OFFTOPIC"
if "@" in grp:
    grp = grp.replace("@", "")
a = API_ID
b = API_HASH
smex = STRING



idk = ""

que = {}

SMEX_USERS = []



async def start_yukki():
    global idk
    global ydk
    global wdk
    global sdk
    global hdk
    global adk
    global bdk
    global cdk
    global ddk
    global edk
    global vkk
    global kkk
    global lkk
    global mkk
    global sid
    global shy
    global aan
    global ake
    global eel
    global khu
    global shi
    global yaa
    global dav
    global raj
    global put

    if smex:
        session_name = str(smex)
        print("String 1 Found")
        idk = TelegramClient(StringSession(session_name), a, b)
        try:
            print("Booting Up The Client 1")
            await idk.start()
            botme = await idk.get_me()
            await idk(functions.channels.JoinChannelRequest(channel="@LegendBot_OP"))
            await idk(functions.channels.JoinChannelRequest(channel="@LegendBot_AI"))
            await idk(functions.channels.JoinChannelRequest(channel=f"@{grp}"))
            botid = telethon.utils.get_peer_id(botme)
            SMEX_USERS.append(botid)
        except Exception as e:
            idk = "smex"
            print(e)
    else:
        print("Session 1 not Found")
        session_name = "startup"
        idk = TelegramClient(session_name, a, b)
        try:
            await idk.start()
        except Exception:
            pass

    
loop = asyncio.get_event_loop()
loop.run_until_complete(start_yukki())


async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass


@idk.on(events.NewMessage(incoming=True, pattern=r"\.join"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.join <Public Channel or Group Link/Username>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = yukki[0]
            text = "Joining..."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("𝐉𝐎𝐢𝐍 𝐇𝐎𝐆𝐘𝐀 𝐕𝐀𝐈 𝐀𝐁 𝐁𝐓𝐀 𝐊𝐈𝐒𝐊𝐈 𝐌𝐀𝐑𝐔😏🔥")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.pjoin"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗣𝗿𝗶𝘃𝗮𝘁𝗲 𝗝𝗼𝗶𝗻\n\nCommand:\n\n.pjoin <Private Channel or Group's access hash>\n\nExample :\nLink = https://t.me/joinchat/HGYs1wvsPUplMmM1\n\n.pjoin HGYs1wvsPUplMmM1"
    if e.sender_id in SMEX_USERS:
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = yukki[0]
            text = "Joining...."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await e.client(ImportChatInviteRequest(bc))
                await event.edit("𝐉𝐎𝐢𝐍 𝐇𝐎𝐆𝐘𝐀 𝐕𝐀𝐈 𝐀𝐁 𝐁𝐓𝐀 𝐊𝐈𝐒𝐊𝐈 𝐌𝐀𝐑𝐔😏🔥")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.leave"))
async def _(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗟𝗲𝗮𝘃𝗲\n\nCommand:\n\n.leave <Channel or Chat ID>"
    if e.sender_id in SMEX_USERS:
        yukki = ("".leave(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) == 7:
            bc = yukki[0]
            bc = int(bc)
            text = "RDX BOT Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Succesfully Left")
            except Exception as e:
                await event.edit(str(e))
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.spam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.delayspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        yukki = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        yukkisexy = yukki[1:]
        if len(yukkisexy) == 2:
            message = str(yukkisexy[1])
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukkisexy[0])
            sleeptime = float(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.bigspam"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(yukki[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.raid"))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗮𝗶𝗱\n\nCommand:\n\n.raid <count> <Username of User>\n\n.raid <count> <reply to a User>\n\nCount must be a integer."
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(yukki) == 2:
            message = str(yukki[1])
            print(message)
            a = await e.client.get_entity(message)
            g = a.id
            c = a.first_name
            username = f"[{c}](tg://user?id={g})"
            counter = int(yukki[0])
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            c = b.first_name
            counter = int(yukki[0])
            username = f"[{c}](tg://user?id={g})"
            for _ in range(counter):
                reply = random.choice(RAID)
                caption = f"{username} {reply}"
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, caption)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True))
async def _(event):
    global que
    queue = que.get(event.sender_id)
    if not queue:
        return
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(0.2)
    async with event.client.action(event.chat_id, "typing"):
        await event.client.send_message(
            entity=event.chat_id,
            message="""{}""".format(random.choice(RRAID)),
            reply_to=event.message.id,
        )


@idk.on(events.NewMessage(incoming=True, pattern=r"\.replyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.replyraid <Username of User>\n\n.replyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 11:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            que[g] = []
            qeue = que.get(g)
            appendable = [g]
            qeue.append(appendable)
            text = "Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.dreplyraid"))
async def _(e):
    global que
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗮𝗰𝘁𝗶𝘃𝗮𝘁𝗲 𝗥𝗲𝗽𝗹𝘆𝗥𝗮𝗶𝗱\n\nCommand:\n\n.dreplyraid <Username of User>\n\n.dreplyraid <reply to a User>"
    if e.sender_id in SMEX_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        yukki = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        await e.get_reply_message()
        if len(e.text) > 12:
            message = str(yukki[0])
            a = await e.client.get_entity(message)
            g = a.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        elif e.reply_to_msg_id:
            a = await e.get_reply_message()
            b = await e.client.get_entity(a.sender_id)
            g = b.id
            try:
                queue = que.get(g)
                queue.pop(0)
            except Exception:
                pass
            text = "De-Activated Reply Raid"
            await e.reply(text, parse_mode=None, link_preview=None)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


@idk.on(events.NewMessage(incoming=True, pattern=r"\.ping"))
async def ping(e):
    if e.sender_id in SMEX_USERS:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"⚡[ᴘᴏɴɢ] ⚡!\n`{ms}` 𝗺𝘀")


@idk.on(events.NewMessage(incoming=True, pattern=r"\.restart"))
async def restart(e):
    if e.sender_id in SMEX_USERS:
        text = "𝙍𝙚𝙨𝙩𝙖𝙧𝙩𝙚𝙙\n\nPlease wait till it reboots..."
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await idk.disconnect()
        except Exception:
            pass
        try:
            await ydk.disconnect()
        except Exception:
            pass
        try:
            await wdk.disconnect()
        except Exception:
            pass
        try:
            await hdk.disconnect()
        except Exception:
            pass
        try:
            await sdk.disconnect()
        except Exception:
            pass
        try:
            await adk.disconnect()
        except Exception:
            pass
        try:
            await bdk.disconnect()
        except Exception:
            pass
        try:
            await cdk.disconnect()
        except Exception:
            pass
        try:
            await ddk.disconnect()
        except Exception:
            pass
        try:
            await edk.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()


@idk.on(events.NewMessage(incoming=True, pattern=r"\.help"))
async def help(e):
    if e.sender_id in SMEX_USERS:
        text = "𝐀𝐕𝐀𝐈𝐋𝐀𝐁𝐋𝐄 𝐂𝐎𝐌𝐌𝐌𝐀𝐍𝐃𝐒 𝐈𝐍 𝐈𝐍𝐂𝐑𝐄𝐃𝐈𝐁𝐋𝐄 𝐒𝐏𝐀𝐌 𝐁𝐎𝐓 \n\n𝐔𝐓𝐈𝐋𝐒 𝐂𝐎𝐌𝐌𝐀𝐍𝐃:\n.ping\n.restart\n\n𝐔𝐒𝐄𝐑𝐁𝐎𝐓 𝐂𝐎𝐌𝐌𝐀𝐍𝐃:\n.bio\n.join\n.pjoin\n.pleave\n\n𝐒𝐏𝐀𝐌 𝐂𝐎𝐌𝐌𝐀𝐍𝐃:\n.spam\n.delayspam\n.bigspam\n.raid\n.replyraid\n.dreplyraid\n\n\nFor more help regarding usage of plugins type plugins name"
        await e.reply(text, parse_mode=None, link_preview=None)


text = """
CONGRATS🥳🥳🥳 YOUR FASTEST, SMOOTHEST AND POWERFUL SPAMBOT DEPLOYED SUCCESSFULLY """

print(text)
print("")
print("🙏🔥🔥YOUR! SPAM BOT STARTED SUCCESFULLY.🔥🔥🙏")
if len(sys.argv) not in (1, 3, 4):
    try:
        idk.disconnect()
    except Exception:
        pass
    try:
        ydk.disconnect()
    except Exception:
        pass
    try:
        wdk.disconnect()
    except Exception:
        pass
    try:
        hdk.disconnect()
    except Exception:
        pass
    try:
        sdk.disconnect()
    except Exception:
        pass
    try:
        adk.disconnect()
    except Exception:
        pass
    try:
        bdk.disconnect()
    except Exception:
        pass
    try:
        cdk.disconnect()
    except Exception:
        pass
    try:
        edk.disconnect()
    except Exception:
        pass
    try:
        ddk.disconnect()
    except Exception:
        pass
    try:
        vkk.disconnect()
    except Exception:
        pass
    try:
        kkk.disconnect()
    except Exception:
        pass
    try:
        lkk.disconnect()
    except Exception:
        pass
    try:
        mkk.disconnect()
    except Exception:
        pass
    try:
        sid.disconnect()
    except Exception:
        pass
    try:
        shy.disconnect()
    except Exception:
        pass
    try:
        aan.disconnect()
    except Exception:
        pass
    try:
        ake.disconnect()
    except Exception:
        pass
    try:
        eel.disconnect()
    except Exception:
        pass
    try:
        khu.disconnect()
    except Exception:
        pass
    try:
        shi.disconnect()
    except Exception:
        pass
    try:
        yaa.disconnect()
    except Exception:
        pass
    try:
        dav.disconnect()
    except Exception:
        pass
    try:
        raj.disconnect()
    except Exception:
        pass
    try:
        put.disconnect()
    except Exception:
        pass
else:
    try:
        idk.run_until_disconnected()
    except Exception:
        pass
    try:
        ydk.run_until_disconnected()
    except Exception:
        pass
    try:
        wdk.run_until_disconnected()
    except Exception:
        pass
    try:
        hdk.run_until_disconnected()
    except Exception:
        pass
    try:
        sdk.run_until_disconnected()
    except Exception:
        pass
    try:
        adk.run_until_disconnected()
    except Exception:
        pass
    try:
        bdk.run_until_disconnected()
    except Exception:
        pass
    try:
        cdk.run_until_disconnected()
    except Exception:
        pass
    try:
        edk.run_until_disconnected()
    except Exception:
        pass
    try:
        ddk.run_until_disconnected()
    except Exception:
        pass
    try:
        vkk.run_until_disconnected()
    except Exception:
        pass
    try:
        kkk.run_until_disconnected()
    except Exception:
        pass
    try:
        lkk.run_until_disconnected()
    except Exception:
        pass
    try:
        mkk.run_until_disconnected()
    except Exception:
        pass
    try:
        sid.run_until_disconnected()
    except Exception:
        pass
    try:
        shy.run_until_disconnected()
    except Exception:
        pass
    try:
        aan.run_until_disconnected()
    except Exception:
        pass
    try:
        ake.run_until_disconnected()
    except Exception:
        pass
    try:
        eel.run_until_disconnected()
    except Exception:
        pass
    try:
        khu.run_until_disconnected()
    except Exception:
        pass
    try:
        shi.run_until_disconnected()
    except Exception:
        pass
    try:
        yaa.run_until_disconnected()
    except Exception:
        pass
    try:
        dav.run_until_disconnected()
    except Exception:
        pass
    try:
        raj.run_until_disconnected()
    except Exception:
        pass
    try:
        put.run_until_disconnected()
    except Exception:
        pass
