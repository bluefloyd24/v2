################################################################
"""
 Mix-Userbot Open Source . Maintained ? Yes Oh No Oh Yes Ngentot
 
 @ CREDIT : NAN-DEV
"""
################################################################


from Mix import bot, get_cgr, ky, nlx, udB

__modles__ = "Alive"
__help__ = get_cgr("help_alive")


@ky.ubot("alive")
async def _(c: nlx, m):
    if not udB.get_var(c.me.id, "gc"):
        gc = await c.get_chats_dialog(c, "grup")
        udB.set_var(c.me.id, "gc", len(gc))
    elif not udB.get_var(c.me.id, "us"):
        us = await c.get_chats_dialog(c, "user")
        udB.set_var(c.me.id, "us", len(us))
    elif not udB.get_var(c.me.id, "bot"):
        bt = await c.get_chats_dialog(c, "bot")
        udB.set_var(c.me.id, "bot", len(bt))
    try:
        x = await c.get_inline_bot_results(bot.me.username, "alive")
        await m.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        await m.reply(error)
