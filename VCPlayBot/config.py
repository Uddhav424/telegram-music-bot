import os
from os import getenv

from dotenv import load_dotenv()

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "1BVtsOHgBu2YnZ7NTf-1L5PXqFzlrVBL_ZebwV2EUPoGw9X36ddkFaOrmjzKI8I0cu4-lRq2VZmVHIieiJ5Ux7o5B9oACE6c3GX2KEz7cP_7WC9IpMF4jxBfw5aNjPRp1BwnM3UeF3cs2THwmB2N67b2w8iOeQpluqru59KOJk60n1rylSVWL4_siEfJZQ4EfszrnaPRYH8LrcONkOt19R37WNoRi2Fs5yJbFDMFWj-TUrl1uA1TJHZcbFdHNwXYgCHhn0oyiUF33dOvtNMK_hSvkchKYw72jCQd3-tdrn4hjMmypigv-BaWG36WCoWIDw_ku8BQ7hIUJPpUO_QgCY8HqSjiLMlo=")
BOT_TOKEN = getenv("8185897011:AAEs215vfIWCekUYcfU4Td79_p0l2GyYEbk")
BOT_NAME = getenv("Shruti x music")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/cutestickersyou")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("API_ID", "20005361"))  
API_HASH = getenv("14553838a536c00979e3f671dd95b047")
BOT_USERNAME = getenv("@Shruti_x_music_bot")
ASSISTANT_NAME = getenv("Shruti x music", "@Shruti_music")
OWNER_NAME = getenv("Tiwari", "@GOODCHEAT0")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/girl_group_chating_group")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("https://t.me/+wJovRaqoZ3lmZjM1", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5096741943").split()))
