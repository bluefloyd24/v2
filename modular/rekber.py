from pyrogram import *
from Mix import *

@ky.ubot("dana")
async def premium(c, m):
    em = Emojik()
    em.initialize()
    await m.reply(cgr("rekber_1").format(em.dana))