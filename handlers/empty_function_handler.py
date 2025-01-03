from telegram import Update
from telegram.ext import ConversationHandler, CallbackQueryHandler, MessageHandler, filters
from functions.empty_function_1.bot import empty_function_1
# from handlers.inline_handler import inline_button_handler
from handlers.start_handler import start_command
from utils.constants import EMPTY_FUNCTION_1, EMPTY_FUNCTION_2


async def ask_param1_empty_function(update: Update, context):
    if update.message.text.lower() == "/start":
        # Reset conversation if /start is typed
        await start_command(update, context)
        return EMPTY_FUNCTION_1

    try:
        print("empty begin")
        context.user_data['param1'] = float(update.message.text)  # Convert the input to float
        print("Empty end")
    except ValueError:
        await update.message.reply_text("Invalid input for param1. Please enter a valid number.")
        return EMPTY_FUNCTION_1

    print("await begin")
    await update.message.reply_text("Please enter the second parameter (param2) for Empty Function 1:")
    print("await end")
    return EMPTY_FUNCTION_2

# Asking for the second parameter (param2) for empty_function_1
async def ask_param2_empty_function(update: Update, context):
    print("empty begin 2")
    if update.message.text.lower() == "/start":
        # Reset conversation if /start is typed
        await start_command(update, context)
        return ConversationHandler.END

    try:
        context.user_data['param2'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param2. Please enter a valid number.")
        return EMPTY_FUNCTION_2

    # Retrieve the parameters from user data
    param1 = context.user_data['param1']
    param2 = context.user_data['param2']

    # Call the empty function
    empty_function_1(param1, param2)

    # Notify user that the function has been executed
    await update.message.reply_text(f"Empty_Function_1 executed with param1={param1} and param2={param2}.")
    return ConversationHandler.END

conv_handler_empty = ConversationHandler(
    entry_points=[MessageHandler(filters.TEXT, ask_param1_empty_function)],
    # entry_points=[CallbackQueryHandler(inline_button_handler, pattern="^empty_function_1$")],
    states={
        EMPTY_FUNCTION_1: [MessageHandler(filters.TEXT, ask_param1_empty_function)],
        EMPTY_FUNCTION_2: [MessageHandler(filters.TEXT, ask_param2_empty_function)],
    },
    fallbacks=[],
)