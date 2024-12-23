# from telegram import Update
# from telegram.ext import CallbackContext
# from utils.constants import EMPTY_FUNCTION_1, ASK_PARAM1
#
# async def start_command(update: Update, context: CallbackContext):
#     i = 0
#     if i == 1:
#         await update.message.reply_text("You are about to start Empty Function 1. Please enter the first parameter.")
#         return EMPTY_FUNCTION_1  # This will start the flow for empty_function_1
#
#     # Alternatively, if you're starting an extended function flow, return its entry state
#     await update.message.reply_text("Choose an option:")
#     return ASK_PARAM1  # This would start the flow for extended function if that's what you want
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


from utils.constants import ASK_PARAM1


async def start_command(update, context):
    context.user_data.clear()
    context.chat_data.clear()
    button1 = InlineKeyboardButton(text="Run my extended function", callback_data="run_extended_function")
    button2 = InlineKeyboardButton(text="Empty Function 1", callback_data="empty_function_1")
    button3 = InlineKeyboardButton(text="Empty Function 2", callback_data="empty_function_2")

    keyboard = InlineKeyboardMarkup([[button1, button2, button3]])
    await update.message.reply_text("Choose an option:", reply_markup=keyboard)
    return ASK_PARAM1
