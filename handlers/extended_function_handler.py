from telegram import Update
from telegram.ext import ConversationHandler

from utils.constants import ASK_PARAM1, ASK_PARAM2, ASK_PARAM3, ASK_PARAM4
from functions.calculation_script.calculation_script import my_function_extended
from handlers.start_handler import start_command


# Asking for the first parameter (param1) for my_function_extended
async def ask_param1_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        # Reset conversation if /start is typed
        await start_command(update, context)
        return ASK_PARAM1

    try:
        context.user_data['param1'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param1. Please enter a valid number.")
        return ASK_PARAM1

    await update.message.reply_text("Please enter the second parameter (param2):")
    return ASK_PARAM2

# Asking for the second parameter (param2) for my_function_extended
async def ask_param2_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        # Reset conversation if /start is typed
        await start_command(update, context)
        return ASK_PARAM1

    try:
        context.user_data['param2'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param2. Please enter a valid number.")
        return ASK_PARAM2

    await update.message.reply_text("Please enter the third parameter (param3):")
    return ASK_PARAM3

# Asking for the third parameter (param3) for my_function_extended
async def ask_param3_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        # Reset conversation if /start is typed
        await start_command(update, context)
        return ASK_PARAM1

    try:
        context.user_data['param3'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param3. Please enter a valid number.")
        return ASK_PARAM3

    await update.message.reply_text("Please enter the fourth parameter (param4):")
    return ASK_PARAM4

# Asking for the fourth parameter (param4) for my_function_extended
async def ask_param4_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        # Reset conversation if /start is typed
        await start_command(update, context)
        return ASK_PARAM1

    try:
        context.user_data['param4'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param4. Please enter a valid number.")
        return ASK_PARAM4

    # Retrieve the parameters from user data
    param1 = context.user_data['param1']
    param2 = context.user_data['param2']
    param3 = context.user_data['param3']
    param4 = context.user_data['param4']

    # Call the extended function with all parameters
    result = my_function_extended(param1, param2, param3, param4)

    # Notify user that the function has been executed
    await update.message.reply_text(f"Extended function executed with result: {result}")
    return ConversationHandler.END
