################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || EH KONTOL KALO PUNYA AKAL DIPAKE YA ANJING GAUSAH APUS² CREDIT MODAL NYOPAS LO BAJINGAN!!
"""
################################################################

from io import BytesIO

import requests
from pyrogram.types import InputMediaPhoto

from Mix import *

__modles__ = "Image"
__help__ = get_cgr("help_img")


async def search_images(query, m, max_results, pros=None):
    url = "https://google-api31.p.rapidapi.com/imagesearch"
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "24d6a3913bmsh3561d6af783658fp1a8240jsneef57a49ff14",
        "X-RapidAPI-Host": "google-api31.p.rapidapi.com",
    }
    try:
        payload = {
            "text": query,
            "safesearch": "off",
            "region": "wt-wt",
            "color": "",
            "size": "",
            "type_image": "",
            "layout": "",
            "max_results": max_results,
        }
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        img_res = response.json().get("result", [])

        media_list = []
        for img_inf in img_res:
            image_url = img_inf.get("image")
            if image_url and image_url.startswith("http"):
                response = requests.get(image_url)
                if response.status_code == 200:
                    img = BytesIO(response.content)
                    media_list.append(InputMediaPhoto(img))

        await m.reply_media_group(media_list, reply_to_message_id=ReplyCheck(m))
    except Exception as e:
        print(f"Error fetching images: {e}")
    finally:
        if pros:
            await pros.delete()


@ky.ubot("image|img")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    try:
        query = ""
        max_results = 3
        if len(m.command) == 2:
            if m.command[1].isdigit():
                max_results = int(m.command[1])
            else:
                query = m.text.split(None, 1)[1]
        elif len(m.command) >= 3:
            if m.command[1].isdigit():
                max_results = int(m.command[1])
                query = m.text.split(None, 2)[2]
            else:
                query = m.text.split(None, 1)[1]
        elif m.reply_to_message:
            query = m.reply_to_message.text
            if len(m.command) == 2:
                max_results = int(m.command[1])
        else:
            return await m.reply(
                f"Contoh penggunaan : `{m.text} 5 kucing lucu` atau `{m.text} kucing lucu`"
            )

        pros = await m.reply(cgr("proses").format(em.proses))
        await search_images(query, m, max_results, pros)
        return
    except Exception as e:
        print(f"Error: {e}")