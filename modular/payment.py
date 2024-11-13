from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from pyrogram import *

from Mix import *

from Mix import bot, get_cgr, ky, nlx

# Variabel global untuk menyimpan link pembayaran
PAYMENT_LINK = "https://t.me/your_default_payment_channel"

@ky.ubot("set_payment")
async def set_payment_command(c, m):
    # Memeriksa apakah ada argumen link yang diberikan setelah perintah .set_payment
    args = m.text.split(maxsplit=1)
    if len(args) < 2:
        await m.reply("Harap berikan link atau username channel pembayaran. Contoh: `.set_payment @bluepay`")
        return
    
    # Mengupdate link pembayaran
    global PAYMENT_LINK
    PAYMENT_LINK = args[1]
    await m.reply(f"Link pembayaran berhasil diperbarui menjadi: {PAYMENT_LINK}")

@ky.ubot("payment")
async def payment_command(c, m):
    # Mengecek apakah ada detail harga dan item
    args = m.text.split(maxsplit=2)
    if len(args) < 3:
        await m.reply("Harap masukkan jumlah dan item pembayaran. Contoh: `.payment 5k baju`")
        return

    # Mengambil jumlah dan item dari argumen
    amount, item = args[1], args[2]
    
    # Pesan konfirmasi awal
    msg = f"Silakan melakukan pembayaran sebesar {amount} untuk item '{item}'. Tekan tombol di bawah untuk melanjutkan ke channel pembayaran."

    # Membuat keyboard dengan tombol Payment
    kb = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Payment", callback_data="payment")]]
    )
    
    # Mengirim pesan dengan tombol Payment
    await m.reply_text(text=msg, reply_markup=kb)
