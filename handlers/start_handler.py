from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from telegram.ext import ConversationHandler


async def start_command(update, context):
    user_name = update.effective_user.first_name

    button1 = InlineKeyboardButton(text="Run my extended function", callback_data="run_extended_function")
    button2 = InlineKeyboardButton(text="Empty Function 1", callback_data="empty_function_1")
    button3 = InlineKeyboardButton(text="Empty Function 2", callback_data="empty_function_2")

    inline_keyboard = [[button1, button2], [button3]]
    inline_markup = InlineKeyboardMarkup(inline_keyboard)

    await update.message.reply_text(
        f"Hello, {user_name}! Welcome to your coin angel. Make your choice:",
        reply_markup=inline_markup
    )

    return ConversationHandler.END
