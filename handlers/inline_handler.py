from telegram.ext import CallbackQueryHandler, ConversationHandler

from handlers.empty_function_handler import ask_param1_empty_function
from handlers.extended_function_handler import ask_param1_extended
from utils.constants import ASK_PARAM1_EXTENDED, EMPTY_FUNCTION_1


async def inline_button_handler(update, context):
    query = update.callback_query
    await query.answer()

    if query.data == "run_extended_function":
        # Start the extended function conversation
        await query.message.reply_text("Please enter the first parameter (param1):")
        return ASK_PARAM1_EXTENDED  # This should trigger the extended function flow

    elif query.data == "empty_function_1":
        # Start the empty function 1 conversation
        await query.message.reply_text("Please enter the first parameter (param1) for Empty Function 1:")
        return EMPTY_FUNCTION_1  # This should trigger the empty function 1 flow

    elif query.data == "empty_function_2":
        # End conversation or handle empty function 2
        await query.message.reply_text("Empty function 2 triggered. Implement later.")
        return ConversationHandler.END