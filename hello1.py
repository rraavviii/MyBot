import telegram.ext
import kiit
import detail
TOKEN = "your token"

def start(update, context):
    update.message.reply_text("You have two choices. Select one of them:\n1. Add\n2. Mul")

def sum(update, context):
    update.message.reply_text("Enter the first number:")
    # Initialize 'operation' key in context.user_data
    context.user_data['operation'] = 'sum'
    # Set a flag to indicate that the first input is being received
    #context.user_data['input_flag'] = 'first'

def mul(update, context):
    update.message.reply_text("Enter the first number:")
    # Initialize 'operation' key in context.user_data
    context.user_data['operation'] = 'mul'
    # Set a flag to indicate that the first input is being received
    context.user_data['input_flag'] = 'first'

def timetable(update, context):
    update.message.reply_text("Enter your roll no:")
    # Initialize 'operation' key in context.user_data
    context.user_data['operation'] = 'timetable'

def handle_input(update, context):
    user_input = update.message.text
    input_flag = context.user_data.get('input_flag', 'first')
    operation = context.user_data.get('operation')
    if operation == 'sum' or operation == 'mul':
        if input_flag == 'first':
            context.user_data['num1'] = int(user_input)
            update.message.reply_text("Enter the second number:")
            # Set the flag to indicate that the second input is being received
            context.user_data['input_flag'] = 'second'

        elif input_flag == 'second':
            context.user_data['num2'] = int(user_input)
            update.message.reply_text("Enter the third number:")
            # Set the flag to indicate that the second input is being received
            context.user_data['input_flag'] = 'third'

        elif input_flag == 'third':
            if operation == 'sum':
                s = kiit.sum(context.user_data['num1'], context.user_data['num2'],int(user_input))
                update.message.reply_text(f"The sum is: {s}")
            elif operation == 'mul':
                s = kiit.mul(context.user_data['num1'], int(user_input))
                update.message.reply_text(f"The product is: {s}")

            # Clear the 'operation' and 'input_flag' keys in context.user_data
            context.user_data.pop('operation', None)
            context.user_data.pop('input_flag', None)

    elif operation == 'timetable':
        s = detail.det(int(user_input))
        update.message.reply_text(f"{s}")

    else:
        update.message.reply_text("Invalid Command. Enter valid Command")

updater = telegram.ext.Updater(TOKEN, use_context=True)

dispatch = updater.dispatcher

dispatch.add_handler(telegram.ext.CommandHandler("start", start))
dispatch.add_handler(telegram.ext.CommandHandler("sum", sum))
dispatch.add_handler(telegram.ext.CommandHandler("mul", mul))
dispatch.add_handler(telegram.ext.CommandHandler("timetable", timetable))

dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_input))

updater.start_polling()
updater.idle()
#
#
# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from telegram.ext import MessageHandler, filters
#
# import json
# import datetime
# import pytz
# import kiit
# import detail
#
# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("You have two choices. Select one of them:\n1. Add\n2. Mul")
#
# async def sum(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("Enter a number:")
#     # Initialize 'operation' key in context.user_data
#     context.user_data['operation'] = 'sum'
#
# async def mul(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("Enter a number:")
#     # Initialize 'operation' key in context.user_data
#     context.user_data['operation'] = 'mul'
#
# async def timetable(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text("Enter your roll no:")
#     # Initialize 'operation' key in context.user_data
#     context.user_data['operation'] = 'timetable'
#
#
# async def handle_input(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     user_input = update.message.text
#     operation = context.user_data.get('operation')
#
#     if operation == 'sum':
#         await update.message.reply_text(f"The sum is: ")
#     elif operation == 'mul':
#         await update.message.reply_text(f"The product is: ")
#     elif operation == 'timetable':
#         s = detail.det(int(user_input))
#         await update.message.reply_text(f"{s}")
#     else:
#         await update.message.reply_text("Enter a valid command: ")
#
# app = ApplicationBuilder().token("6832286166:AAFlWnEY2fTKABtldlcWO18QJUddWlTB-z0").build()
# app.add_handler(CommandHandler("start", start))
# app.add_handler(CommandHandler("sum", sum))
# app.add_handler(CommandHandler("mul", mul))
# app.add_handler(CommandHandler("timetable", timetable))
# app.add_handler(MessageHandler(filters.ALL, handle_input))
# app.run_polling()
#


# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
#
# # Replace 'YOUR_BOT_TOKEN' with your actual bot token
# TOKEN = 'your token'
#
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Welcome to the Calculator Bot! Type /add to add two numbers or /sub to subtract.')
#
# def add(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Enter the first number:')
#     context.user_data['operation'] = 'add'
#
# def sub(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text('Enter the first number:')
#     context.user_data['operation'] = 'sub'
#
# def process_number(update: Update, context: CallbackContext) -> None:
#     user_input = update.message.text
#     try:
#         number = float(user_input)
#         context.user_data['number'] = number
#
#         if context.user_data['operation'] == 'add':
#             update.message.reply_text('Enter the second number:')
#             return
#         elif context.user_data['operation'] == 'sub':
#             update.message.reply_text('Enter the second number:')
#             return
#
#     except ValueError:
#         update.message.reply_text('Invalid input. Please enter a valid number.')
#
# def calculate_result(update: Update, context: CallbackContext) -> None:
#     user_input = update.message.text
#     try:
#         number = float(user_input)
#
#         if context.user_data['operation'] == 'add':
#             result = context.user_data['number'] + number
#         elif context.user_data['operation'] == 'sub':
#             result = context.user_data['number'] - number
#
#         update.message.reply_text(f'Result: {result}')
#
#     except ValueError:
#         update.message.reply_text('Invalid input. Please enter a valid number.')
#
# def main() -> None:
#     updater = Updater(TOKEN)
#     dp = updater.dispatcher
# 
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(CommandHandler("add", add))
#     dp.add_handler(CommandHandler("sub", sub))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, process_number))
#     dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate_result))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()

