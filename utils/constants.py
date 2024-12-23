import os
from dotenv import load_dotenv

load_dotenv()

ASK_PARAM1, ASK_PARAM2, ASK_PARAM3, ASK_PARAM4, EMPTY_FUNCTION_1, EMPTY_FUNCTION_2, BUTTTON_HANDLER = range(7)
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_ANGEL_TOKEN")
