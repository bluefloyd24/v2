from Mix import *

@ky.ubot("dana")
async def premium(c, m):
    em = Emojik()
    em.initialize()
    if m.from_user.id not in DEVS:
        return await m.reply(cgr("rekber_1").format(em.dana))