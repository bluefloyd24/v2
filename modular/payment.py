from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import asyncio

from pyrogram import *

from Mix import *


# Define the PAYMENT variable with a default link (can be updated with the .set_payment command)
PAYMENT = "https://t.me/your_payment_channel"  # Replace with your actual default link

@ky.ubot("payment")
async def payment_command(c: nlx, m):
    # Extract the command arguments
    args = m.text.split(maxsplit=1)[1] if len(m.text.split()) > 1 else None
    if not args:
        await m.reply("Please specify an amount and recipient, e.g., .payment 5k ganom usa.")
        return

    try:
        # Split arguments into amount and recipient
        amount, *recipient = args.split()
        recipient = ' '.join(recipient)
    except ValueError:
        await m.reply("Incorrect format. Use: .payment <amount> <recipient>.")
        return

    # Format the reply message
    message_text = f"Silahkan transfer {amount} untuk {recipient}. Klik tombol di bawah untuk menuju ke channel pembayaran."

    # Create an inline button that links to the payment channel specified in the PAYMENT variable
    payment_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Payment", url=PAYMENT)]
        ]
    )

    # Send the reply with the inline button
    await m.reply(message_text, reply_markup=payment_button)

@ky.ubot("set_payment")
async def set_payment_command(c: nlx, m):
    # Extract the link argument
    link = m.text.split(maxsplit=1)[1] if len(m.text.split()) > 1 else None
    if not link:
        await m.reply("Please provide a payment link, e.g., .set_payment https://t.me/your_payment_channel.")
        return
    
    global PAYMENT
    PAYMENT = link
    await m.reply(f"Payment link updated to: {PAYMENT}")
