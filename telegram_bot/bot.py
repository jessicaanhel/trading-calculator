# import os
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
# from telegram.ext import (
#     Application,
#     CommandHandler,
#     CallbackQueryHandler,
#     ConversationHandler,
#     MessageHandler,
#     filters,
# )
#
# from dotenv import load_dotenv
#
# load_dotenv()
# TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_ANGEL_TOKEN")
#
#
# if TELEGRAM_BOT_TOKEN is not None:
#     print(TELEGRAM_BOT_TOKEN[-5:])
# else:
#     print("TELEGRAM_ANGEL_TOKEN is None")
#
# # Define states (we add more states for the new parameters)
# ASK_PARAM1, ASK_PARAM2, EMPTY_FUNCTION_1, EMPTY_FUNCTION_2 = range(4)
#
# # Command for /start
# async def start_command(update: Update, context):
#     context.user_data.clear()  # Clear the context data to reset everything
#     context.chat_data.clear()  # Clear chat data if necessary
#     # Send a message with 3 buttons
#     button1 = InlineKeyboardButton(text="Run my extended function", callback_data="run_extended_function")
#     button2 = InlineKeyboardButton(text="Empty Function 1", callback_data="empty_function_1")
#     button3 = InlineKeyboardButton(text="Empty Function 2", callback_data="empty_function_2")
#
#     keyboard = InlineKeyboardMarkup([[button1, button2, button3]])  # Add all buttons to the keyboard
#     await update.message.reply_text("Choose an option:", reply_markup=keyboard)
#
#     # Reset the conversation state
#     return ASK_PARAM1  # Go back to the first step of the conversation flow
#
# # Handler for button clicks
# async def inline_button_handler(update: Update, context):
#     query = update.callback_query
#     await query.answer()  # Acknowledge the callback query
#
#     # Handle the different button actions
#     if query.data == "run_extended_function":
#         await query.message.reply_text("Please enter the first parameter (param1):")
#         return ASK_PARAM1
#
#     elif query.data == "empty_function_1":
#         # Initiate asking for parameters for the empty function
#         await query.message.reply_text("Please enter the first parameter (param1) for Empty Function 1:")
#         return EMPTY_FUNCTION_1
#
#     elif query.data == "empty_function_2":
#         await query.message.reply_text("Empty function 2 triggered. Implement later.")
#         return ConversationHandler.END
#
# # Asking for the first parameter (param1) for empty_function_1
# async def ask_param1_empty_function(update: Update, context):
#     if update.message.text.lower() == "/start":
#         # Reset conversation if /start is typed
#         await start_command(update, context)
#         return ASK_PARAM1
#
#     try:
#         context.user_data['param1'] = float(update.message.text)  # Convert the input to float
#     except ValueError:
#         await update.message.reply_text("Invalid input for param1. Please enter a valid number.")
#         return EMPTY_FUNCTION_1
#
#     await update.message.reply_text("Please enter the second parameter (param2) for Empty Function 1:")
#     return EMPTY_FUNCTION_1
#
# # Asking for the second parameter (param2) for empty_function_1
# async def ask_param2_empty_function(update: Update, context):
#     if update.message.text.lower() == "/start":
#         # Reset conversation if /start is typed
#         await start_command(update, context)
#         return ASK_PARAM1
#
#     try:
#         context.user_data['param2'] = float(update.message.text)  # Convert the input to float
#     except ValueError:
#         await update.message.reply_text("Invalid input for param2. Please enter a valid number.")
#         return EMPTY_FUNCTION_1
#
#     # Retrieve the parameters from user data
#     param1 = context.user_data['param1']
#     param2 = context.user_data['param2']
#
#     # Call the empty function
#     empty_function_1(param1, param2)
#
#     # Notify user that the function has been executed
#     await update.message.reply_text(f"Empty Function 1 executed with param1={param1} and param2={param2}.")
#     return ConversationHandler.END
#
# # Empty function 1 (implement later)
# def empty_function_1(param1, param2):
#     print(f"Executing Empty Function 1 with param1={param1} and param2={param2}")
#     # Implement your function logic here
#
# # Example extended function
# def my_function_extended(param1, param2, param3, param4):
#     result = param1 + param2 + param3 + param4
#     return result
#
# # Conversation handler
# conv_handler = ConversationHandler(
#     entry_points=[CommandHandler("start", start_command)],  # Start command
#     states={
#         ASK_PARAM1: [MessageHandler(filters.TEXT, ask_param1_empty_function)],
#         EMPTY_FUNCTION_1: [MessageHandler(filters.TEXT, ask_param2_empty_function)],
#     },
#     fallbacks=[],
# )
#
# def main():
#     # Setup the bot
#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
#
#     # Add handlers
#     application.add_handler(conv_handler)
#     application.add_handler(CallbackQueryHandler(inline_button_handler))
#
#     # Start the bot
#     application.run_polling()
#
# if __name__ == "__main__":
#     main()