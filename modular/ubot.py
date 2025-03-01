from datetime import datetime, timedelta
from Mix import *
from thegokil import DEVS

@ky.ubot("ubotv1|ubotv2")
async def userbot_activation(c, m):
    em = Emojik()
    em.initialize()
    if m.from_user.id not in DEVS:
        return await m.reply(cgr("ubot_2").format(em.gagal))
    
    args = m.text.split(maxsplit=2)
    
    if len(args) < 2:
        return await m.reply(cgr("ubot_3").format(em.gagal))
    
    try:
        duration = int(args[1])  # Durasi dalam hari
    except ValueError:
        return await m.reply(cgr("ubot_4").format(em.gagal))
    
    if not m.reply_to_message:
        return await m.reply("❌ Harap balas pesan pengguna yang ingin diaktifkan userbotnya.")
    
    target_user = m.reply_to_message.from_user
    target_id = target_user.id
    target_mention = f"<a href='tg://user?id={target_id}'>{target_user.first_name}</a>"
    
    # Tentukan versi berdasarkan perintah yang digunakan
    command = m.text.split()[0].lstrip(".")
    version = "1" if "ubotv1" in command else "2"
    
    # Hitung tanggal berakhir
    end_date = (datetime.now() + timedelta(days=duration)).strftime("%d-%m-%Y")
    
    # Teks pesan
    message_text = cgr("ubot_1").format(target_mention, version, duration, end_date)
    
    # Path atau URL gambar
    image_path = "Mix/core/ubotss.jpg"  # Ganti dengan path lokal atau URL gambar
    
    # Kirim pesan dengan gambar
    await c.send_photo(
        chat_id=m.chat.id,
        photo=image_path,
        caption=message_text
    )

@ky.ubot("form")
async def form_install_userbot(c, m):
    """
    Mengirimkan format form untuk install userbot
    """
    message = (
        "`残酷 ━━━━━ × 𝗙𝗢𝗥𝗠 𝗜𝗡𝗦𝗧𝗔𝗟𝗟 𝗨𝗦𝗘𝗥𝗕𝗢𝗧!\n\n"
        "ㅤ× ━━ Username :\n"
        "ㅤ× ━━ Nomor :\n"
        "ㅤ× ━━ 2FA :\n"
        "ㅤ× ━━ Durasi :\n"
        "ㅤ× ━━ Versi : 1/2\n\n"
        "** jika tidak ada 2FA/pass kosongkan\n"
        "** buy with your own risk!`"
    )
    await m.reply(message)
