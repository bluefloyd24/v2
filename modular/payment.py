from pyrogram.enums import *
from pyrogram.types import *

from Mix import *

__modles__ = "Payment"
__help__ = get_cgr("help_payme")


@ky.ubot("markdown")
async def _(c: nlx, m):
    try:
        xi = await c.get_inline_bot_results(bot.me.username, "pay_in")
        await m.delete()
        await c.send_inline_bot_result(
            m.chat.id, xi.query_id, xi.results[0].id, reply_to_message_id=ReplyCheck(m)
        )
    except Exception as e:
        await m.edit(f"{e}")
        return
