import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pytgcalls import PyTgCalls

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")
    
# Necessary Vars
API_ID = int(os.getenv("API_ID", "20005361"))
API_HASH = os.getenv("API_HASH", "14553838a536c00979e3f671dd95b047")
SESSION = os.getenv("1BVtsOHgBu2YnZ7NTf-1L5PXqFzlrVBL_ZebwV2EUPoGw9X36ddkFaOrmjzKI8I0cu4-lRq2VZmVHIieiJ5Ux7o5B9oACE6c3GX2KEz7cP_7WC9IpMF4jxBfw5aNjPRp1BwnM3UeF3cs2THwmB2N67b2w8iOeQpluqru59KOJk60n1rylSVWL4_siEfJZQ4EfszrnaPRYH8LrcONkOt19R37WNoRi2Fs5yJbFDMFWj-TUrl1uA1TJHZcbFdHNwXYgCHhn0oyiUF33dOvtNMK_hSvkchKYw72jCQd3-tdrn4hjMmypigv-BaWG36WCoWIDw_ku8BQ7hIUJPpUO_QgCY8HqSjiLMlo=")
HNDLR = os.getenv("HNDLR", "/")
GROUP_MODE = os.getenv("GROUP_MODE", "True")


contact_filter = filters.create(
    lambda _, __, message:
    (message.from_user and message.from_user.is_contact) or message.outgoing
)


if GROUP_MODE == ("True" or "true"):
    grp = True
else:
    grp = False

GRPPLAY = grp
bot = Client(SESSION, API_ID, API_HASH, plugins=dict(root="VCBot"))
call_py = PyTgCalls(bot)
