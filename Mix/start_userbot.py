import sys
from pyrogram import Client
import logging
from team.nandev.class_log import LOGS # Menambahkan impor class_log

# Hybrid logger setup
def setup_logger(user_id):
    # Menggunakan logger dari class_log
    logger = class_log.LOGG(f"userbot_{user_id}")
    return logger


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 start_userbot.py <user_id> <session_string>")
        sys.exit(1)

    user_id = sys.argv[1]
    session_string = sys.argv[2]
    LOGGER = setup_logger(user_id)

    LOGGER.info("Memulai userbot...")
    try:
        app = Client(session_string=session_string)
        app.run()  # Menjalankan userbot
    except Exception as e:
        LOGGER.error(f"Terjadi kesalahan saat menjalankan userbot: {e}")
        sys.exit(1)
