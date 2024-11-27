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


@ky.callback("clbk.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    op = get_bahasa_()
    user_name = f"<a href='tg://user?id={cq.from_user.id}'>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>"

    if cmd == "bhsa":
        await cq.edit_message_text("who r u")
    elif cmd == "rebot":
        if cq.from_user.id != nlx.me.id:
            await cq.edit_message_text(cgr("asst_12"))
            return
        await cq.edit_message_text(cgr("reboot_1"))
        os.execl(sys.executable, sys.executable, "-m", "Mix")
    elif cmd == "bek":
        await clbk_start(c, cq)
    elif cmd == "bantuan":
        button = ikb([[(cgr("balik"), "clbk.bek")]])
        await cq.edit_message_text(cgr("asst_11"), reply_markup=button)
    elif cmd == "clos":
        await close_button_handler(c, cq)
    elif cmd == "fitur":
        await clbk_fitur(c, cq)
    elif cmd == "status":
       if cq.from_user.id != nlx.me.id:
          await cq.edit_message_text(cgr("asst_12"))
          return
       await cq.edit_message_text(cgr("asst_13"))


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
            [(cgr("asst_7"), "clbk.status"), (cgr("asst_8"), "clbk.fitur"), (cgr("asst_10"), "clbk.bantuan")],
        ]
    )) 

async def close_button_handler(c, cq):
    await cq.message.delete()
    return

async def clbk_fitur(c, cq):
    user_id = cq.from_user.id
    emut = await nlx.get_prefix(user_id)
    msg = (
        "<b>Commands\n      Prefixes: `{}`\n      Modules: <code>{}</code></b>".format(
            " ".join(emut), len(CMD_HELP)
        )
    )

    # Mengedit pesan yang ada dan menampilkan daftar perintah serta tombol navigasi
    await cq.edit_message_text(
        text=msg,
        reply_markup=InlineKeyboardMarkup(
            paginate_modules(0, CMD_HELP, "help")  # Tombol navigasi modul
        ),
    )


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
