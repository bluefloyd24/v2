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

bot = Bot()
nlx = Userbot()


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

    # Minta input nomor akun
        await login_user(c, cq, user_id)

async def login_user(bot, chat_id, user_id):
    try:
        # Step 1: Meminta nomor telepon
        await bot.send_message(chat_id, "💬 Masukkan nomor akun Anda (contoh: +62813xxxx):")
        phone_message: Message = await bot.listen(chat_id, timeout=300)
        phone_number = phone_message.text

        # Step 2: Memulai client sementara untuk login
        temp_client = Client(
            name="temp_login",
            api_id="25048157",   # Masukkan API ID dari konfigurasi Anda
            api_hash="f7af78e020826638ce203742b75acb1b",  # Masukkan API Hash dari konfigurasi Anda
            in_memory=True
        )
        await temp_client.start()
        await temp_client.send_code(phone_number)

        # Step 3: Meminta kode login
        await bot.send_message(chat_id, "📩 Masukkan kode login yang dikirimkan ke nomor Anda:")
        code_message: Message = await bot.listen(chat_id, timeout=300)
        login_code = code_message.text

        # Step 4: Verifikasi kode login
        try:
            await temp_client.sign_in(phone_number, login_code)
        except PhoneCodeInvalid:
            await bot.send_message(chat_id, "❌ Kode login salah. Silakan coba lagi.")
            return
        except PhoneCodeExpired:
            await bot.send_message(chat_id, "❌ Kode login kedaluwarsa. Silakan coba lagi.")
            return

        # Step 5: Menangani 2FA jika diperlukan
        try:
            await temp_client.check_password("")  # Cek apakah butuh password
        except SessionPasswordNeeded:
            await bot.send_message(chat_id, "🔒 Masukkan password untuk verifikasi 2 langkah:")
            password_message: Message = await bot.listen(chat_id, timeout=300)
            password = password_message.text
            await temp_client.check_password(password)

        # Step 6: Mengambil session string
        session_string = await temp_client.export_session_string()
        await temp_client.stop()

        # Step 7: Simpan session string ke database
        udB.add_ubot(
            user_id=user_id,
            api_id="YOUR_API_ID",
            api_hash="YOUR_API_HASH",
            session_string=session_string
        )

        # Step 8: Instal userbot
        await bot.send_message(chat_id, "🚀 Userbot berhasil dibuat, menginstal...")
        await install_userbot(user_id, session_string)

        # Selesai
        await bot.send_message(chat_id, "✅ Userbot berhasil diinstal dan siap digunakan.")
    except Exception as e:
        await bot.send_message(chat_id, f"❌ Terjadi kesalahan: {e}")



async def install_userbot(user_id, session_string):
    """
    Fungsi untuk menginstal userbot setelah mendapatkan session string.
    """
    try:
        userbot_dir = "userbots"
        session_name = f"userbot_{user_id}.session"
        userbot_session_path = os.path.join(userbot_dir, session_name)

        # Membuat direktori untuk userbot jika belum ada
        if not os.path.exists(userbot_dir):
            os.makedirs(userbot_dir)

        # Mengecek apakah session sudah ada
        if os.path.exists(userbot_session_path):
            LOGGER.warning(f"Userbot untuk {user_id} sudah terinstal.")
            return "Userbot sudah terinstal."

        # Membuat session dan memulai aplikasi Pyrogram
        async with Client(userbot_session_path, api_id=API_ID, api_hash=API_HASH, session_string=session_string) as app:
            LOGGER.info(f"Memulai userbot untuk {user_id}...")
            await app.start()
            await app.send_message(user_id, "💻 Userbot telah diinstall dan siap digunakan!")
            LOGGER.info(f"Userbot untuk {user_id} berhasil diinstal!")
            return "Userbot berhasil diinstall!"
    except Exception as e:
        LOGGER.error(f"Error saat menginstall userbot untuk {user_id}: {e}")
        return f"❌ Gagal menginstall userbot: {e}"

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
