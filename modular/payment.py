from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from pyrogram import *

from Mix import *

# Ganti dengan link channel pembayaran kamu
PAYMENT = "https://t.me/your_payment_channel"  # Link pembayaran default

@ky.ubot("payment")
async def payment_command(c, m):
    # Teks konfirmasi pembayaran
    message_text = "Klik tombol di bawah untuk melakukan pembayaran."

    # Inline button menuju channel pembayaran
    payment_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Payment", url=PAYMENT)]  # Tombol Payment
        ]
    )

    # Mengirim pesan dengan tombol Payment
    await m.reply_text(message_text, reply_markup=payment_button)

@ky.ubot("set_payment")
async def set_payment_command(c, m):
    # Mengganti link channel pembayaran melalui command
    link = m.text.split(maxsplit=1)[1] if len(m.text.split()) > 1 else None
    if not link:
        await m.reply("Silakan masukkan link pembayaran, contoh: .set_payment https://t.me/your_payment_channel")
        return
    
    global PAYMENT
    PAYMENT = link
    await m.reply(f"Link pembayaran telah diperbarui menjadi: {PAYMENT}")
