################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV || MIKIR GOBLOK, TOLOL, IDIOT, NGENTOT, KONTOL, BAJINGAN
  • JANGAN DIHAPUS YA MONYET-MONYET SIALAN
"""
################################################################

import os
import random
from asyncio import sleep

import requests

from Mix import *

__modles__ = "Katanime"
__help__ = get_cgr("help_katnim")


def carikatanime(katanya):
    pea = ["1", "2", "3", "4", "5"]
    hal = random.choice(pea)
    url = f"https://katanime.vercel.app/api/carikata?kata={katanya}&page={hal}"
    res = requests.get(url)
    if res.status_code == 200:
        bisul = res.json()
        results = bisul.get("result", [])
        percobaan = 15
        dicoba = 0
        while dicoba < percobaan:
            try:
                ambil1 = random.choice(results)
                anim = ambil1.get("anime", "")
                karak = ambil1.get("character", "")
                kata = ambil1.get("indo", "")
                akhir = cgr("katnim_1").format(anim, karak, kata)
                return akhir
            except IndexError:
                dicoba += 1
        return cgr("katnim_2")
    else:
        print(f"error {res.status_code} {res.text}")


def ambil_katanime():
    url = f"https://katanime.vercel.app/api/getrandom"
    res = requests.get(url)
    if res.status_code == 200:
        bisul = res.json()
        results = bisul.get("result", [])
        ambil1 = random.choice(results)
        anim = ambil1.get("anime", "")
        karak = ambil1.get("character", "")
        kata = ambil1.get("indo", "")
        akhir = cgr("katnim_1").format(anim, karak, kata)
        return akhir
    else:
        return cgr("katnim_3").format(res.status_code, res.text)


def getbyanime(tokoh):
    pea = ["1", "2", "3", "4", "5"]
    hal = random.choice(pea)
    url = f"https://katanime.vercel.app/api/getbyanime?anime={tokoh}&page={hal}"
    res = requests.get(url)
    if res.status_code == 200:
        bisul = res.json()
        results = bisul.get("result", [])
        percobaan = 15
        dicoba = 0
        while dicoba < percobaan:
            try:
                bisul = res.json()
                results = bisul.get("result", [])
                ambil1 = random.choice(results)
                anim = ambil1.get("anime", "")
                karak = ambil1.get("character", "")
                kata = ambil1.get("indo", "")
                akhir = cgr("katnim_1").format(anim, karak, kata)
                return akhir
            except IndexError:
                dicoba += 1
        return cgr("katnim_2")
    else:
        print(f"error {res.status_code} {res.text}")


def animelist():
    url = f"https://katanime.vercel.app/api/getlistanime"
    res = requests.get(url)
    daftar = []
    if res.status_code == 200:
        bisul = res.json()
        results = bisul.get("result", [])
        for isi in results:
            anim = isi.get("anime", "")
            kata = isi.get("totalKata", "")
            akhir = cgr("katnim_4").format(anim, kata)
            daftar.append(akhir)
        return "".join(daftar)
    else:
        print(f"error {res.status_code} {res.text}")


@ky.ubot("kata")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    arg = c.get_text(m)
    mek = await m.reply(cgr("proses").format(em.proses))
    if len(m.command) > 1 and not m.reply_to_message:
        cari_kata = getbyanime(arg)
        await sleep(0.5)
        await m.reply(cari_kata, reply_to_message_id=ReplyCheck(m))
    elif len(m.command) == 1 and m.reply_to_message:
        cari_kata = getbyanime(arg)
        await sleep(0.5)
        await m.reply(cari_kata, reply_to_message_id=ReplyCheck(m))
    else:
        await m.reply(cgr("katnim_5").format(em.gagal))
    await mek.delete()


@ky.ubot("katanime|katanimelist")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    arg = c.get_text(m)
    mek = await m.reply(cgr("proses").format(em.proses))
    if m.command[0] == "katanimelist":
        ambil_anime = animelist()
        if len(ambil_anime) > 4096:
            file = open("DaftarAnime.txt", "w+")
            file.write(ambil_anime)
            file.close()
            await m.reply_document(
                "DaftarAnime.txt",
                caption=cgr("katnim_6"),
                reply_to_message_id=ReplyCheck(m),
            )
            os.remove("DaftarAnime.txt")
        else:
            await m.reply(ambil_anime)
    elif len(m.command) > 1 and not m.reply_to_message:
        cari_kata = carikatanime(arg)
        await sleep(0.5)
        await m.reply(cari_kata, reply_to_message_id=ReplyCheck(m))
    elif len(m.command) == 1 and not m.reply_to_message:
        cari_random = ambil_katanime()
        await sleep(0.5)
        await m.reply(cari_random, reply_to_message_id=ReplyCheck(m))
    elif len(m.command) == 1 and m.reply_to_message:
        cari_kata = carikatanime(arg)
        await sleep(0.5)
        await m.reply(cari_kata, reply_to_message_id=ReplyCheck(m))
    else:
        await m.reply(cgr("katnim_7").format(em.gagal))
    await mek.delete()
