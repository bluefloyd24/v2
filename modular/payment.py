from pyrogram import *
from pyrogram.errors import *
from pyrogram.enums import *
from pyrogram.types import *
from Mix import *

__modles__ = "Payment"
__help__ = get_cgr("help_payme")

# Variabel untuk menyimpan pesan dinamis pengguna
@ky.ubot("setcgrpay1")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    babi = await m.reply(cgr("proses").format(em.proses))
    await asyncio.sleep(2)
    user_id = c.me.id
    direp = m.reply_to_message
    args_txt = c.get_arg(m)

    # Mengambil pesan dari pesan balasan atau argumen
    if direp:
        payment_msg = direp.text
    else:
        payment_msg = args_txt

    # Jika tidak ada pesan yang diberikan, batalkan proses
    if not payment_msg:
        return await babi.edit(cgr("gcs_1").format(em.gagal))

    # Menyimpan pesan ke database udB
    udB.set_var(user_id, "payment_message", payment_msg)
    await babi.edit(cgr("payme_2").format(em.sukses, payment_msg))
    return


@ky.ubot("payment")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    try:
        xi = await c.get_inline_bot_results(bot.me.username, "payme_in")
        await c.reply_inline_bot_result(xi.query_id, xi.results[0].id)
    except Exception as e:
        await m.edit(f"{e}")
        return
