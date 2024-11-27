################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


import os
import sys

from pyrogram import *
from pyrogram.enums import *
from pyrogram.helpers import ikb
from pyrogram.types import *

from Mix import *


def st_lang():
    languages = get_bahasa_()
    keyboard = ikb(
        [[(f"{lang['natively']}", f"set_{lang['code']}") for lang in languages]]
    )
    keb = ikb([[("Back", "clbk.bek"), ("Close", "clbk.clos")]])
    for row in keb.inline_keyboard:
        keyboard.inline_keyboard.append(row)
    return keyboard


@ky.callback("close_asst")
async def _(c, cq):
    await cq.edit_message_text(cgr("asstcls"))


@ky.callback("clbk.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    op = get_bahasa_()
    user_name = f"<a href='tg://user?id={cq.from_user.id}'>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>"

    if cmd == "bhsa":
        meki = f"{op[0]['natively']}"
        teks = cgr("asst_4").format(meki)
        await cq.edit_message_text(text=teks, reply_markup=st_lang())
    elif cmd == "rebot":
        # Hanya pemilik bot yang dapat melakukan reboot
        if cq.from_user.id != nlx.me.id:
            await cq.answer("who are you?", True)
            return
        await cq.edit_message_text(cgr("reboot_1"))
        os.execl(sys.executable, sys.executable, "-m", "Mix")
    elif cmd == "bek":
        # Memanggil fungsi clbk_start untuk kembali ke menu utama
        await clbk_start(c, cq)
    elif cmd == "bantuan":
        await cq.edit_message_text(cgr("asst_11"))
    elif cmd == "clos":
        await close_button_handler(c, cq)

# Fungsi clbk_start yang digunakan untuk kembali ke menu utama
async def clbk_start(c, cq):
    # Ambil data pengguna (opsional, jika diperlukan)
    user_name = f"<a href='tg://user?id={cq.from_user.id}'>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>"

    # Pesan untuk menu utama
    ts_1 = cgr("asst_2").format(user_name)  # Format pesan dengan nama pengguna

    # Kembali ke menu utama
    await cq.edit_message_text(text=ts_1, reply_markup=ikb(
        [
            [(cgr("asst_9"), "clbk.buat"), (cgr("asst_6"), "clbk.rebot")],
            [(cgr("asst_7"), "clbk.status"), (cgr("asst_8"), "clbk.fitur"), (cgr("asst_3"), "clbk.bhsa")],
            [(cgr("asst_10"), "clbk.bantuan")],
        ]
    )) 

async def close_button_handler(c, cq):
    await cq.message.delete()
    return

@ky.callback("clbk.status")
async def _(c, cq):
    if db.check_premium(cq.from_user.id):
        premium_data = db.get_premium_info(cq.from_user.id)
        end_time = premium_data["premium_end"]
        time_left = end_time - datetime.utcnow()
        await cq.edit_message_text(f"Status: Premium\nDurasi: {time_left.days} hari lagi")
    else:
        await cq.edit_message_text("Anda bukan pengguna premium.")


@ky.callback("^set_(.*?)")
async def _(c, cq):
    lang_code = cq.data.split("_")[1]
    op = get_bahasa_()
    sl = next((ox for ox in op if ox["code"] == lang_code), None)
    kb = ikb([[(cgr("balik"), "clbk.bek")]])
    if sl:
        ndB.set_key("bahasa", lang_code)
        await cq.edit_message_text(
            cgr("asst_5").format(sl["natively"]), reply_markup=kb
        )
    else:
        LOGGER.error(f"Language with code '{lang_code}' not found.")

@ky.callback("^clbk.balek$")
async def kembali_handler(c, cq):
    # Panggil kembali handler `/start` untuk menampilkan menu awal
    await start_handler(c, cq.message)


@ky.callback("^clbk.clos$")
async def close_handler(c, cq):
    # Menghapus pesan ketika tombol "Close" ditekan
    await cq.message.delete()
