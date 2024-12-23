from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from handlers.start_handler import start_command
from handlers.inline_handler import inline_button_handler
from handlers.extended_function_handler import ask_param1_extended, ask_param2_extended, ask_param3_extended, ask_param4_extended
from handlers.empty_function_handler import ask_param1_empty_function, ask_param2_empty_function
from utils.constants import ASK_PARAM1, ASK_PARAM2, ASK_PARAM3, ASK_PARAM4, EMPTY_FUNCTION_1, EMPTY_FUNCTION_2, TELEGRAM_BOT_TOKEN


if TELEGRAM_BOT_TOKEN is not None:
    print(TELEGRAM_BOT_TOKEN[-5:])
else:
    print("TELEGRAM_ANGEL_TOKEN is None")

extended_function = True

# if extended_function:
#     conv_handler_extended = ConversationHandler(
#         entry_points=[CommandHandler("start", start_command)],
#         states={
#             ASK_PARAM1: [MessageHandler(filters.TEXT, ask_param1_extended)],
#             ASK_PARAM2: [MessageHandler(filters.TEXT, ask_param2_extended)],
#             ASK_PARAM3: [MessageHandler(filters.TEXT, ask_param3_extended)],
#             ASK_PARAM4: [MessageHandler(filters.TEXT, ask_param4_extended)],
#         },
#         fallbacks=[],
#     )

# Empty Function Conversation Handler
conv_handler_empty = ConversationHandler(
    entry_points=[CommandHandler("start", start_command)],
    states={
        EMPTY_FUNCTION_1: [MessageHandler(filters.TEXT, ask_param1_empty_function)],
        EMPTY_FUNCTION_2: [MessageHandler(filters.TEXT, ask_param2_empty_function)],
    },
    fallbacks=[],
)

def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # if extended_function:
    #     application.add_handler(conv_handler_extended)

    application.add_handler(conv_handler_empty)
    application.add_handler(CallbackQueryHandler(inline_button_handler))

    application.run_polling()

if __name__ == "__main__":
    main()
