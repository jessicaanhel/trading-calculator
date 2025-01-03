from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from handlers.inline_handler import inline_button_handler
from handlers.extended_function_handler import ask_param1_extended, ask_param2_extended, ask_param3_extended, \
    ask_param4_extended
from handlers.empty_function_handler import ask_param1_empty_function, ask_param2_empty_function
from utils.constants import (
    ASK_PARAM1_EXTENDED,
    ASK_PARAM2_EXTENDED,
    ASK_PARAM3_EXTENDED,
    ASK_PARAM4_EXTENDED,
    TELEGRAM_BOT_TOKEN, EMPTY_FUNCTION_1, EMPTY_FUNCTION_2)
from warnings import filterwarnings
from telegram.warnings import PTBUserWarning


if TELEGRAM_BOT_TOKEN is not None:
    print(TELEGRAM_BOT_TOKEN[-5:])
else:
    print("TELEGRAM_ANGEL_TOKEN is None")

extended_function = True
filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

conv_handler_extended = ConversationHandler(
    entry_points=[CallbackQueryHandler(inline_button_handler, pattern="^run_extended_function$")],
    states={
        ASK_PARAM1_EXTENDED: [MessageHandler(filters.TEXT, ask_param1_extended)],
        ASK_PARAM2_EXTENDED: [MessageHandler(filters.TEXT, ask_param2_extended)],
        ASK_PARAM3_EXTENDED: [MessageHandler(filters.TEXT, ask_param3_extended)],
        ASK_PARAM4_EXTENDED: [MessageHandler(filters.TEXT, ask_param4_extended)],
    },
    fallbacks=[],
)

# Empty function 1 conversation handler
conv_handler_empty_1 = ConversationHandler(
    entry_points=[CallbackQueryHandler(inline_button_handler, pattern="^empty_function_1$")],
    states={
        EMPTY_FUNCTION_1: [MessageHandler(filters.TEXT, ask_param1_empty_function)],
        EMPTY_FUNCTION_2: [MessageHandler(filters.TEXT, ask_param2_empty_function)],
    },
    fallbacks=[],
)


def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

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