from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from handlers.inline_handler import inline_button_handler
from handlers.extended_function_handler import ask_param1_extended, ask_param2_extended, ask_param3_extended, \
    ask_param4_extended, conv_handler_extended
from handlers.empty_function_handler import ask_param1_empty_function, ask_param2_empty_function, conv_handler_empty_1
from handlers.start_handler import start_command
from utils.constants import (
    ASK_PARAM1_EXTENDED,
    ASK_PARAM2_EXTENDED,
    ASK_PARAM3_EXTENDED,
    ASK_PARAM4_EXTENDED,
    TELEGRAM_BOT_TOKEN, EMPTY_FUNCTION_1, EMPTY_FUNCTION_2)


if TELEGRAM_BOT_TOKEN is not None:
    print("Token is correct:" , TELEGRAM_BOT_TOKEN[-5:])
else:
    print("TELEGRAM_ANGEL_TOKEN is None")

extended_function = True


def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start_command))
    # Add handlers for different workflows
    application.add_handler(conv_handler_extended)
    application.add_handler(conv_handler_empty_1)

    # Add CallbackQueryHandler separately for inline button handling
    application.add_handler(CallbackQueryHandler(inline_button_handler, pattern="^run_extended_function$"))
    application.add_handler(CallbackQueryHandler(inline_button_handler, pattern="^empty_function_1$"))
    application.add_handler(CallbackQueryHandler(inline_button_handler, pattern="^empty_function_2$"))


    application.run_polling()

if __name__ == "__main__":
    main()