from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from pyrogram import *

from Mix import *

from Mix import bot, get_cgr, ky, nlx

__modles__ = "Payment"
__help__ = get_cgr("help_payment")

# Link pembayaran (ganti dengan link channel pembayaran kamu)
PAYMENT_LINK = "https://t.me/bbluepay" 

@ky.ubot("payment")
async def payment_command(c: nlx, m):
    try:
        # Mengambil hasil inline bot untuk payment
        x = await c.get_inline_bot_results(bot.me.username, "payment")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await m.reply(str(error))


@ky.callback(("^payment_info"))
async def payment_info_callback(c, cq):
    # Mengirimkan teks informasi pembayaran dengan tombol pembayaran
    txt = "Silakan klik tombol di bawah untuk menuju ke channel pembayaran."
    payment_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Payment", url=PAYMENT_LINK)]
        ]
    )
    await cq.edit_message_text(txt, reply_markup=payment_button)
