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

        await login_user(c, cq, user_id)

import asyncio
from pyrogram import Client
from pyrogram.handlers import MessageHandler

async def ask_user_input(client: Client, chat_id: int, prompt: str, timeout: int = 60):
    # Kirim prompt ke pengguna
    await client.send_message(chat_id, prompt)

    # Asynchronous event loop to wait for user input
    event = asyncio.Event()
    response = None

    # Fungsi handler untuk menangani respon pengguna
    def message_handler(client, message):
        nonlocal response
        if message.chat.id == chat_id:
            response = message.text.strip()  # Simpan pesan yang diterima
            event.set()  # Tandai bahwa pesan diterima

    # Menambahkan handler untuk menangani pesan
    client.add_handler(MessageHandler(message_handler))

    try:
        # Tunggu hingga event terpenuhi (pesan diterima)
        await asyncio.wait_for(event.wait(), timeout)
        if response:
            return response
        else:
            raise Exception("Tidak ada respons dari pengguna.")
    except asyncio.TimeoutError:
        raise Exception("Waktu habis. Pengguna tidak merespons dalam waktu yang ditentukan.")
    finally:
        # Hapus handler setelah selesai, pastikan hanya satu kali
        try:
            client.remove_handler(message_handler)
        except ValueError:
            pass  # If handler is already removed, no need to worry


# Fungsi utama untuk login userbot
async def login_user(bot: Client, cq: CallbackQuery, userbot: Client, user_id: int):
    chat_id = cq.message.chat.id

    try:
        # Step 1: Meminta nomor telepon
        phone_number = await ask_user_input(bot, chat_id, "💬 Masukkan nomor akun Anda (contoh: +62813xxxx):")
        print(f"Nomor telepon diterima: {phone_number}")

        # Step 2: Kirim kode login
        await userbot.send_code(phone_number)

        # Step 3: Meminta kode login dari pengguna
        login_code = await ask_user_input(bot, chat_id, "📩 Masukkan kode login yang dikirimkan ke nomor Anda:")
        print(f"Kode login diterima: {login_code}")

        # Step 4: Masuk
        try:
            await userbot.sign_in(phone_number, login_code)
        except userbot.SessionPasswordNeeded:
            # Jika 2FA aktif
            password = await ask_user_input(bot, chat_id, "🔒 Masukkan password untuk verifikasi 2 langkah:")
            await userbot.check_password(password)

        # Step 5: Ambil session string
        session_string = await userbot.export_session_string()
        print("Session string berhasil diambil.")

        # Step 6: Simpan session string
        udB.add_ubot(
            user_id=user_id,
            api_id=userbot.api_id,
            api_hash=userbot.api_hash,
            session_string=session_string
        )

        # Step 7: Instal userbot
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
