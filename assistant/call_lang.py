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
from thegokil import DEVS

from Mix import *


@ky.callback("clbk.")
async def _(c, cq):
    cmd = cq.data.split(".")[1]
    op = get_bahasa_()
    user_id = cq.from_user.id
    premium_status = udB.check_premium(user_id)
    ubot_status = udB.has_userbot(user_id)
    user_name = f"<a href='tg://user?id={cq.from_user.id}'>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>"

    if cmd == "bhsa":
        await cq.edit_message_text("who r u")

    elif cmd == "rebot":
        lggn = ikb([[(cgr("lgnn"), "https://t.me/zavril", "url")]])
        bwat = ikb([[(cgr("asst_9"), "clbk.buat")]])
        if not premium_status["is_premium"]:
            
            await cq.edit_message_text(cgr("asst_12"), reply_markup=lggn)
            return

        if not ubot_status:

            await cq.edit_message_text(cgr("reboot_2"), reply_markup=bwat)
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
        button = ikb([[(cgr("balik"), "clbk.bek")]])
        user_name = f"<a href='tg://user?id={cq.from_user.id}'>{cq.from_user.first_name} {cq.from_user.last_name or ''}</a>"
        remaining_days = premium_status["remaining_days"]
  
        if cq.from_user.id in DEVS:
            await cq.edit_message_text(cgr("devs"))
            return

        if not premium_status["is_premium"]:
            await cq.edit_message_text(cgr("asst_14").format(user_name, remaining_days), reply_markup=button)
            return
         
        await cq.edit_message_text(cgr("asst_13").format(user_name, remaining_days), reply_markup=button)

    elif cmd == "buat":
        lggn = ikb([[(cgr("lgnn"), "https://t.me/zavril", "url")]])
        if not premium_status["is_premium"]:
            
            await cq.edit_message_text(cgr("asst_12"), reply_markup=lggn)
            return

        if udB.has_userbot(user_id):
            await cq.answer("✅ Userbot sudah aktif untuk akun ini.", show_alert=True)
            return

        # Memulai proses pembuatan userbot
        await cq.message.reply("💬 Masukkan nomor akun Anda (contoh: +62813xxxx):")

        @ky.on_message(filters.private & filters.text & filters.reply)
        async def get_phone(client, message):
            if message.reply_to_message and "Masukkan nomor akun" in message.reply_to_message.text:
                phone_number = message.text
                await message.reply("📩 Masukkan kode login:")

                @ky.on_message(filters.private & filters.text & filters.reply)
                async def get_login_code(client, message_code):
                    if message_code.reply_to_message and "Masukkan kode login" in message_code.reply_to_message.text:
                        login_code = message_code.text
                        await message_code.reply("🔒 Masukkan kode 2FA (jika ada). Jika tidak, kirim '-'.")

                        @ky.on_message(filters.private & filters.text & filters.reply)
                        async def get_2fa_code(client, message_2fa):
                            if message_2fa.reply_to_message and "Masukkan kode 2FA" in message_2fa.reply_to_message.text:
                                twofa_code = message_2fa.text
                                if twofa_code == "-":
                                    twofa_code = None

                                await message_2fa.reply("🔄 Memulai login session...")

                                # Backend: Generate session string
                                try:
                                    from pyrogram import Client

                                    async with Client(
                                        phone_number,  # Nomor telepon dari pengguna
                                        api_id=API_ID,  # API ID bot atau default
                                        api_hash=API_HASH,  # API Hash bot atau default
                                        phone_code=login_code,  # Kode login yang diberikan
                                        password=twofa_code  # 2FA jika ada
                                    ) as app:
                                        session_string = await app.export_session_string()

                                        # Simpan data ke database
                                        udB.add_ubot(user_id, API_ID, API_HASH, session_string)

                                        await message_2fa.reply(
                                            "✅ Login session berhasil.\n\n"
                                            "⏳ Tunggu 1-2 menit untuk menginstall userbot..."
                                        )

                                        # Proses instalasi userbot
                                        await install_userbot(user_id, session_string)
                                        await message_2fa.reply("🚀 Userbot berhasil diinstall!")
                                except Exception as e:
                                    await message_2fa.reply(
                                        f"❌ Terjadi kesalahan saat login: {e}\n\n"
                                        "Pastikan data yang dimasukkan sudah benar."
                                    )
                                    return


async def install_userbot(user_id, session_string):
    try:
        # Logika untuk instalasi userbot
        # Misalnya, menjalankan subprocess untuk userbot
        process = await asyncio.create_subprocess_exec(
            "python3", "start_userbot.py",  # Script instalasi userbot
            str(user_id),  # ID pengguna
            session_string,  # String session Pyrogram v2
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode == 0:
            print(f"Userbot berhasil diinstall untuk {user_id}: {stdout.decode()}")
        else:
            print(f"Error instalasi userbot untuk {user_id}: {stderr.decode()}")
    except Exception as e:
        print(f"Terjadi kesalahan saat instalasi userbot untuk {user_id}: {e}")


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
    if cq.message:  # Pastikan pesan masih ada
        try:
            await cq.message.delete()  # Hapus pesan
        except Exception as e:
            await cq.answer(f"Gagal menghapus pesan: {str(e)}", show_alert=True)
    else:
        await cq.answer("Pesan sudah tidak ditemukan.", show_alert=True)


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
