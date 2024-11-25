from pyrogram import *
from pyrogram.errors import *
from pyrogram.enums import *
from pyrogram.types import *
from Mix import *

__modles__ = "Payment"
__help__ = get_cgr("help_payme")

DEVS = [6037364404]

@ky.ubot("payment")
async def _(c: nlx, m):
    em = Emojik()
    em.initialize()
    user_id = m.from_user.id
    if user_id not in DEVS:
        await m.reply(cgr("payme_2").format(em.gagal))
        return

    
    try:
        xi = await c.get_inline_bot_results(bot.me.username, "payme_in")
        await c.send_inline_bot_result(m.chat.id, xi.query_id, xi.results[0].id, reply_to_message_id=ReplyCheck(m))
    except Exception as e:
        await m.edit(f"{e}")
        return
