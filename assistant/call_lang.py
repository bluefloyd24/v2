################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################

import os
import sys
import asyncio
import logging
from pyrogram.errors import FloodWait, PhoneCodeInvalid, PhoneCodeExpired, SessionPasswordNeeded
from pyrogram import Client
from pyrogram import *
from pyrogram.enums import *
from pyrogram.helpers import ikb
from pyrogram.types import *
from thegokil import DEVS

from Mix import *
from Mix.mix_client import *

LOGGER = logging.getLogger("install_userbot")

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
        if cq.from_user.id in DEVS:

            await cq.edit_message_text(cgr("reboot_1"))
            os.execl(sys.executable, sys.executable, "-m", "Mix")
         
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
        lnjtkn = ikb(
            [
                [(cgr("lnjt"), "clbk.lanjut")],
                [(cgr("balik"), "clbk.bek")],
            ]
        )

        if cq.from_user.id in DEVS:
            await cq.edit_message_text(cgr("devs"))
            return

        await cq.edit_message_text(
            """
𝗕𝗟𝗨𝗘𝗙𝗟𝗢𝗬𝗗-Userbot.
<blockquote>⋟ **Ketentuan:**
• ID Telegram dengan awal 1/2/5 atau ID lama di bawah 2022.
• Untuk ID 6/7 pastikan akun tersebut aktif digunakan selama 3-4 bulan.
• Tidak dipergunakan untuk hal-hal negatif.
• Tidak melanggar ToS dari Telegram.

⋟ **Penyebab terjadinya banned di akun Telegram yang menggunakan userbot di antaranya:**
• Melanggar ketentuan dari Telegram.
• Adanya pemakaian tidak wajar dari fitur yang ada di userbot.
• Terdeteksi adanya aktivitas yang mencurigakan.
• Laporan atau pengaduan dari pihak lain.

⋟ **Note:**
Jika menggunakan fitur Dspam/Delayspam, pastikan mengatur delay di atas 5 menit atau di atas 300 detik guna mengurangi risiko akun terbanned!.

⋟ **Garansi:**
Untuk akun yang terbanned/deactive bisa klaim garansi. Akun yang sudah membuat userbot tidak bisa membuatnya lagi (1x pembuatan per user).

⋟ **Buy with your own risk!**
Silakan pilih lanjutkan jika setuju dan paham dengan ketentuan yang berlaku.</blockquote>
""",
        reply_markup=lnjtkn,
    )
     
    elif cmd == "lanjut":
        lggn = ikb([[(cgr("lgnn"), "https://t.me/zavril", "url")]])

    # Periksa status premium
        if not premium_status["is_premium"]:
            await cq.edit_message_text(cgr("asst_12"), reply_markup=lggn)
            return

    # Periksa apakah userbot sudah aktif
        if ubot_status:
            await cq.edit_message_text(cgr("asst_15"))
            return
        user_id = cq.from_user.id
        await login_user(c, cq, user_id)

async def login_user(bot: Client, cq: CallbackQuery, user_id: int):
    chat_id = cq.message.chat.id

    # Koleksi database tempat menyimpan sementara input pengguna
    login_data_collection = udB["login_data"]

    try:
        # Step 1: Meminta nomor telepon pengguna
        await bot.send_message(chat_id, "💬 Masukkan nomor akun Anda (contoh: +62813xxxx):")
        phone_message = await bot.listen(chat_id, timeout=60)
        phone_number = phone_message.text.strip()
        print(f"Nomor telepon diterima: {phone_number}")

        # Simpan nomor telepon ke database
        login_data_collection.update_one(
            {"user_id": user_id},
            {"$set": {"phone_number": phone_number}},
            upsert=True
        )

        # Step 2: Membuat client sementara untuk login
        temp_client = Client(
            name="temp_login",
            api_id=25048157,  # Ganti dengan API ID Anda
            api_hash="f7af78e020826638ce203742b75acb1b",  # Ganti dengan API Hash Anda
            in_memory=True
        )
        await temp_client.start()
        await temp_client.send_code(phone_number)

        # Step 3: Meminta kode login
        await bot.send_message(chat_id, "📩 Masukkan kode login yang dikirimkan ke nomor Anda:")
        code_message = await bot.listen(chat_id, timeout=60)
        login_code = code_message.text.strip()
        print(f"Kode login diterima: {login_code}")

        # Simpan kode login ke database
        login_data_collection.update_one(
            {"user_id": user_id},
            {"$set": {"login_code": login_code}},
            upsert=True
        )

        # Step 4: Verifikasi login
        try:
            await temp_client.sign_in(phone_number, login_code)
        except temp_client.SessionPasswordNeeded:
            # Jika 2FA aktif, minta password
            await bot.send_message(chat_id, "🔒 Masukkan password untuk verifikasi 2 langkah:")
            password_message = await bot.listen(chat_id, timeout=60)
            password = password_message.text.strip()

            # Simpan password ke database
            login_data_collection.update_one(
                {"user_id": user_id},
                {"$set": {"password": password}},
                upsert=True
            )
            await temp_client.check_password(password)

        # Step 5: Ambil session string
        session_string = await temp_client.export_session_string()
        await temp_client.stop()
        print("Session string berhasil diambil.")

        # Simpan session string ke database
        udB.add_ubot(
            user_id=user_id,
            api_id=25048157,
            api_hash="f7af78e020826638ce203742b75acb1b",
            session_string=session_string
        )

        # Step 6: Instal userbot
        await bot.send_message(chat_id, "🚀 Userbot berhasil dibuat, menginstal...")
        await install_userbot(user_id, session_string)

        # Hapus data login sementara dari database
        login_data_collection.delete_one({"user_id": user_id})

        # Selesai
        await bot.send_message(chat_id, "✅ Userbot berhasil diinstal dan siap digunakan.")

    except asyncio.TimeoutError:
        # Jika user tidak merespon
        await bot.send_message(chat_id, "❌ Waktu habis. Silakan coba lagi.")
        login_data_collection.delete_one({"user_id": user_id})  # Hapus data sementara
    except Exception as e:
        # Tangani semua error
        await bot.send_message(chat_id, f"❌ Terjadi kesalahan: {e}")
        login_data_collection.delete_one({"user_id": user_id})  # Hapus data sementara

async def install_userbot(user_id: int, session_string: str):
    """
    Fungsi untuk menginstal userbot menggunakan session string pengguna.
    """
    try:
        # Membuat instance Pyrogram dengan session string
        userbot_client = Client(
            session_name=session_string,
            api_id=25048157,  # Ganti dengan API ID Anda
            api_hash="f7af78e020826638ce203742b75acb1b",  # Ganti dengan API Hash Anda
        )

        # Mulai userbot
        await userbot_client.start()
        print(f"✅ Userbot untuk user_id {user_id} berhasil dijalankan.")

        # Simpan log atau status bahwa userbot berhasil diinstal
        log_collection = udB["userbot_logs"]
        log_collection.update_one(
            {"user_id": user_id},
            {"$set": {"status": "installed", "last_started": datetime.utcnow()}},
            upsert=True
        )

        # Log ke konsol
        print(f"Userbot berhasil diinstal untuk user_id {user_id}.")

    except Exception as e:
        print(f"❌ Terjadi kesalahan saat menginstal userbot: {e}")
        raise e

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
