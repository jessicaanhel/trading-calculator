from telegram import Update
from telegram.ext import ConversationHandler

from handlers.start_handler import start_command


async def reset_and_start(update: Update, context):
    context.user_data.clear()
    context.chat_data.clear()
    await start_command(update, context)
    return ConversationHandler.END