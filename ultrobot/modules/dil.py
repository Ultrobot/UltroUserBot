

from ultrobot.cmdhelp import CmdHelp
from ultrobot import PLUGIN_CHANNEL_ID, CMD_HELP
from ultrobot.events import register
from re import search
from json import loads, JSONDecodeError
from ultrobot.language import LANGUAGE_JSON
from os import remove

# ██████ LANGUAGE CONSTANTS ██████ #

from ultrobot.language import get_value
LANG = get_value("dil")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.dil ?(.*)")
@register(outgoing=True, pattern="^.lang ?(.*)")
async def dil(event):
    global LANGUAGE_JSON

    komut = event.pattern_match.group(1)
    if search(r"y[uü]kle|install", komut):
        await event.edit("`Dil dosyası yükleniyor...`")
        if event.is_reply:
            reply = await event.get_reply_message()
            dosya = await reply.download_media()

            if ((len(reply.file.name.split(".")) >= 2) and (not reply.file.name.split(".")[1] == "ultrojson")):
                return await event.edit("`Lütfen geçerli bir` **UltroJSON** `dosyası verin!`")

            try:
                dosya = loads(open(dosya, "r").read())
            except JSONDecodeError:
                return await event.edit("`Lütfen geçerli bir` **UltroJSON** `dosyası verin!`")

            await event.edit(f"`{dosya['LANGUAGE']}` `dili yükleniyor...`")
            pchannel = await event.client.get_entity(PLUGIN_CHANNEL_ID)

            dosya = await reply.download_media(file="./ultrobot/language/")
            dosya = loads(open(dosya, "r").read())
            await reply.forward_to(pchannel)
            
            LANGUAGE_JSON = dosya
            await event.edit(f"✅ `{dosya['LANGUAGE']}` `dili başarıyla yüklendi!`\n\n**İşlemlerin geçerli olması için botu yeniden başlatın!**")
        else:
            await event.edit("**Lütfen bir dil dosyasına yanıt verin!**")
    elif search(r"bilgi|info", komut):
        await event.edit("`Dil dosyası bilgileri getiriliyor... Lütfen bekleyiniz.`")
        if event.is_reply:
            reply = await event.get_reply_message()
            if ((len(reply.file.name.split(".")) >= 1) and (not reply.file.name.split(".")[1] == "ultrojson")):
                return await event.edit("`Lütfen geçerli bir` **UltroJSON** `dosyası verin!`")

            dosya = await reply.download_media()

            try:
                dosya = loads(open(dosya, "r").read())
            except JSONDecodeError:
                return await event.edit("`Lütfen geçerli bir` **UltroJSON** `dosyası verin!`")

            await event.edit(
                f"**Dil: **`{dosya['LANGUAGE']}`\n"
                f"**Dil Kodu: **`{dosya['LANGCODE']}`\n"
                f"**Çevirmen: **`{dosya['AUTHOR']}`\n"

                f"\n\n`Dil dosyasını yüklemek için` `.dil yükle` `yazın`"
            )
        else:
            await event.edit("**Lütfen bir dil dosyasına yanıt verin!**")
    else:
        await event.edit(
            f"**🪙 Dil: **`{LANGUAGE_JSON['LANGUAGE']}`\n"
            f"**🔋 Dil Kodu: **`{LANGUAGE_JSON['LANGCODE']}`\n"
            f"**⌨️ Çeviren: **`{LANGUAGE_JSON ['AUTHOR']}`\n"
        )

CmdHelp('dil').add_command(
    'dil', None, LANG['DİL1']
).add_command(
    'dil bilgi', None, LANG['DİL2']
).add_command(
    'dil yükle', None, LANG['DİL3']
).add()
