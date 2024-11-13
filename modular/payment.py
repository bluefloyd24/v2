from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from pyrogram import *

from Mix import *

from Mix import bot, get_cgr, ky, nlx

# Link pembayaran (ganti dengan link channel pembayaran kamu)
PAYMENT_LINK = "https://t.me/your_payment_channel" 

@ky.ubot("payment")
async def payment_command(c: nlx, m):
    # Teks untuk informasi pembayaran
    message_text = "Silakan klik tombol di bawah untuk menuju ke channel pembayaran."

    # Membuat tombol inline dengan satu tombol "Payment"
    payment_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Payment", url=PAYMENT_LINK)]
        ]
    )

    # Mengirim pesan dengan tombol "Payment"
    await m.reply_text(message_text, reply_markup=payment_button)
