################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

import os
import random
from io import BytesIO

from aiohttp import ClientSession

from Mix import *
from Mix.core.tools_quote import *

__modles__ = "Carbon"
__help__ = get_cgr("help_carbon")


anj = ClientSession()


async def buat_bon(code, bgne, theme, language):
    url = "https://carbonara.solopov.dev/api/cook"
    json_data = {
        "code": code,
        "paddingVertical": "56px",
        "paddingHorizontal": "56px",
        "backgroundMode": "color",
        "backgroundColor": bgne,
        "theme": theme,
        "language": language,
        "fontFamily": "Cascadia Code",
        "fontSize": "14px",
        "windowControls": True,
        "widthAdjustment": True,
        "lineNumbers": True,
        "firstLineNumber": 1,
        "name": "Mix-Userbot-Carbon",
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=json_data) as resp:
            image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@ky.ubot("carbon|carbonara")
async def _(c, m):
    em = Emojik()
    em.initialize()
    rep = m.reply_to_message
    text = None
    if rep:
        text = m.reply_to_message.text or m.reply_to_message.caption
    if not text:
        return await m.reply(
            cgr("crbn_1").format(em.gagal, m.text, m.text, m.text, m.text)
        )
    ex = await m.reply(cgr("proses").format(em.proses))
    try:
        if rep:
            if len(m.command) == 1:
                acak = random.choice(loanjing)
                tem = random.choice(loanjing)
                meg = await buat_bon(text, acak, "python", tem)
                with open("carbon.png", "wb") as f:
                    f.write(meg.getvalue())
                await m.reply_photo(
                    "carbon.png",
                    caption=cgr("crbn_2").format(
                        em.sukses, nlx.me.mention, reply_to_message_id=ReplyCheck(m)
                    ),
                )
                os.remove("carbon.png")
            elif len(m.command) == 2:
                warna = m.text.split(None, 1)[1] if len(m.command) > 1 else None
                if warna:
                    acak = warna
                else:
                    acak = random.choice(loanjing)
                tem = random.choice(loanjing)
                meg = await buat_bon(text, acak, "python", tem)
                with open("carbon.png", "wb") as f:
                    f.write(meg.getvalue())
                await m.reply_photo(
                    "carbon.png",
                    caption=cgr("crbn_2").format(
                        em.sukses, nlx.me.mention, reply_to_message_id=ReplyCheck(m)
                    ),
                )
                os.remove("carbon.png")
            else:
                warna = (
                    m.text.split(None, len(m.command) - 1)[1]
                    if len(m.command) > 1
                    else None
                )
                if warna:
                    acak = warna
                else:
                    acak = random.choice(loanjing)
                tema = (
                    m.text.split(None, len(m.command) - 1)[2]
                    if len(m.command) > 2
                    else None
                )
                if tema:
                    tem = tema
                else:
                    tem = random.choice(loanjing)
                lague = (
                    m.text.split(None, len(m.command) - 1)[3]
                    if len(m.command) > 3
                    else "python"
                )
                meg = await buat_bon(text, acak, lague, tem)
                with open("carbon.png", "wb") as f:
                    f.write(meg.getvalue())
                await m.reply_photo(
                    "carbon.png",
                    caption=cgr("crbn_2").format(
                        em.sukses, nlx.me.mention, reply_to_message_id=ReplyCheck(m)
                    ),
                )
                os.remove("carbon.png")

        else:
            text = m.command[1:]
    except Exception as e:
        await m.reply(f"Terjadi kesalahan: {str(e)}")
    finally:
        await ex.delete()
        if "meg" in locals():
            meg.close()


@ky.ubot("bglist")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    jadi = cgr("qot_1").format(em.sukses) + "\n".join(
        [f"<b>{i+1}</b> <code>{theme}</code>" for i, theme in enumerate(loanjing)]
    )
    if len(jadi) > 4096:
        with open("bglist.txt", "w") as file:
            file.write("\n".join(loanjing))
        await m.reply_document("bglist.txt", caption=cgr("qot_2").format(em.sukses))
        os.remove("bglist.txt")
    else:
        await pros.edit(jadi)


@ky.ubot("temlist")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    pros = await m.reply(cgr("proses").format(em.proses))
    jadi = cgr("them_1").format(em.sukses) + "\n".join(
        [f"<b>{i+1}</b> <code>{theme}</code>" for i, theme in enumerate(tempik)]
    )
    if len(jadi) > 4096:
        with open("temlist.txt", "w") as file:
            file.write("\n".join(tempik))
        await m.reply_document("temlist.txt", caption=cgr("them_2").format(em.sukses))
        os.remove("temlist.txt")
    else:
        await pros.edit(jadi)
