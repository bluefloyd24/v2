from pyrogram import *
from pyrogram.types import *

from Mix import *

__modles__ = "Games"
__help__ = get_cgr("help_games")


@ky.ubot("catur")
async def _(c, m):
    try:
        x = await c.get_inline_bot_results("GameFactoryBot")
        msg = m.reply_to_message or m
        await c.send_inline_bot_result(
            m.chat.id, x.query_id, x.results[0].id, reply_to_message_id=msg.id
        )
    except Exception as error:
        await m.reply(error)


@ky.ubot("dice")
async def _(c, m):
    await c.send_dice(m.chat.id, "🎲")
    await m.delete()


@ky.ubot("dart")
async def _(c, m):
    await c.send_dice(m.chat.id, "🎯")
    await m.delete()


@ky.ubot("basket")
async def _(c, m):
    await c.send_dice(m.chat.id, "🏀")
    await m.delete()


@ky.ubot("bowling")
async def _(c, m):
    await c.send_dice(m.chat.id, "🎳")
    await m.delete()


@ky.ubot("football")
async def _(c, m):
    await c.send_dice(m.chat.id, "⚽")
    await m.delete()


@ky.ubot("slot")
async def _(c, m):
    await c.send_dice(m.chat.id, "🎰")
    await m.delete()
