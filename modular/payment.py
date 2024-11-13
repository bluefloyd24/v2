# payment.py
from pyrogram.enums import *
from pyrogram.types import *
from Mix import *

__modles__ = "Payment"
__help__ = get_cgr("help_payme")

# Variabel untuk menyimpan pesan dinamis pengguna
payment_message = "Ini adalah channel pembayaran default. Silakan atur pesan dengan .setcgrpay1"

@ky.ubot("setcgrpay1")
async def set_payment_message(c, m):
    global payment_message
    args = m.text.split(maxsplit=1)
    
    # Cek apakah pengguna memasukkan pesan
    if len(args) < 2:
        await m.reply("Harap masukkan pesan. Contoh: `.setcgrpay1 ini adalah channel pembayaran saya t.me/bbluepay`")
        return
    
    # Atur pesan pembayaran dengan teks baru
    payment_message = args[1]
    await m.reply("Pesan pembayaran berhasil diatur.")

@ky.ubot("payment")
async def _(c: nlx, m):
    try:
        xi = await c.get_inline_bot_results(bot.me.username, "payme_in")
        await m.delete()
        await c.send_inline_bot_result(
            m.chat.id, xi.query_id, xi.results[0].id, reply_to_message_id=ReplyCheck(m)
        )
    except Exception as e:
        await m.edit(f"{e}")
        return
