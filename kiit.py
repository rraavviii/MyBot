def add(roll):
    sum=0
    for digit in str(roll):
        sum += int(digit)
    return sum

def mul(roll1,roll2,roll3):
    m=roll1*roll2*roll3
    return m
# import telegram.ext
# import kiit
# import result
# import detail
#
# TOKEN = "6832286166:AAFlWnEY2fTKABtldlcWO18QJUddWlTB-z0"
#
# # Define a dictionary to store user data
# user_data_dict = {}
#
#
# def start(update, context):
#     update.message.reply_text("Enter your choice. Select one of them:\n1. \timetable\n2. \sgpa .")
#
#
# def timetable(update, context):
#     update.message.reply_text("Enter your roll no:")
#     context.user_data['operation'] = 'timetable'
#
#
# def sgpa(update, context):
#     update.message.reply_text("Enter your roll no:")
#     context.user_data['operation'] = 'sgpa'
#     # Initialize a list to store subject credits
#     context.user_data['subject_credits'] = []
#
#     # Ask the first question
#     update.message.reply_text("Enter credits for the first subject:")
#
#
# def handle_input(update, context):
#     user_input = update.message.text
#     operation = context.user_data.get('operation')
#
#     if operation == 'timetable':
#         s = detail.det(int(user_input))
#         update.message.reply_text(f"{s}")
#
#     elif operation == 'sgpa':
#         # Check if subject credits are being collected
#         if 'subject_credits' in context.user_data:
#             # Add the subject credits to the list
#             context.user_data['subject_credits'].append(float(user_input))
#
#             # Check if all questions have been asked
#             if len(context.user_data['subject_credits']) < 5:  # Assuming 5 subjects for example
#                 # Ask the next question
#                 update.message.reply_text(
#                     f"Enter credits for the next subject ({len(context.user_data['subject_credits']) + 1}):")
#             else:
#                 # Calculate SGPA and reply to the user
#                 total_credits = sum(context.user_data['subject_credits'])
#                 sgpa_result = result.res(total_credits)
#                 update.message.reply_text(f"Your SGPA: {sgpa_result}")
#
#                 # Clear user data
#                 del context.user_data['subject_credits']
#                 del context.user_data['operation']
#         else:
#             update.message.reply_text("Invalid state. Please start over.")
#
#     else:
#         update.message.reply_text("Enter a valid command.")
#
#
# updater = telegram.ext.Updater(TOKEN, use_context=True)
#
# dispatch = updater.dispatcher
#
# dispatch.add_handler(telegram.ext.CommandHandler("start", start))
# dispatch.add_handler(telegram.ext.CommandHandler("timetable", timetable))
# dispatch.add_handler(telegram.ext.CommandHandler("sgpa", sgpa))
#
# dispatch.add_handler(
#     telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_input))
#
# updater.start_polling()
# updater.idle()


# import telegram.ext
# import kiit
# import result
# import detail
#
# TOKEN = "6832286166:AAFlWnEY2fTKABtldlcWO18QJUddWlTB-z0"
#
# # Define a dictionary to store user data
# user_data_dict = {}
#
# def start(update, context):
#     update.message.reply_text("Enter your choice. Select one of them:\n1. \timetable\n2. \sgpa .")
#
# def timetable(update, context):
#     update.message.reply_text("Enter your roll no:")
#     context.user_data['operation'] = 'timetable'
#
# def sgpa(update, context):
#     update.message.reply_text("Enter your roll no:")
#     context.user_data['operation'] = 'sgpa'
#
# def ask_roll_number(update, context):
#     user_input = update.message.text
#     context.user_data['roll_no'] = int(user_input)
#     # Initialize a list to store subject credits
#     context.user_data['subject_credits'] = []
#
#     # Ask the first question for subject credits
#     update.message.reply_text("Enter credits for the first subject:")
#
# def ask_total_credit(update, context):
#     user_input = update.message.text
#     context.user_data['total_credit'] = int(user_input)
#
#
# def handle_input(update, context):
#     user_input = update.message.text
#     operation = context.user_data.get('operation')
#
#     if operation == 'timetable':
#         s = detail.det(int(user_input))
#         update.message.reply_text(f"{s}")
#
#     elif operation == 'sgpa':
#         # Check if roll number is collected
#         if 'roll_no' not in context.user_data:
#             ask_roll_number(update, context)
#
#         else:
#             # Add the subject credits to the list
#             context.user_data['subject_credits'].append(float(user_input))
#
#             # Check if all questions have been asked
#             if len(context.user_data['subject_credits']) < 5:  # Assuming 5 subjects for example
#                 # Ask the next question
#                 update.message.reply_text(f"Enter credits for the next subject ({len(context.user_data['subject_credits']) + 1}):")
#             else:
#                 # Calculate SGPA and reply to the user
#                 total_credits = sum(context.user_data['subject_credits'])
#                 sgpa_result = result.res(total_credits)
#                 update.message.reply_text(f"Your SGPA: {sgpa_result}")
#
#                 # Clear user data
#                 del context.user_data['roll_no']
#                 del context.user_data['subject_credits']
#                 del context.user_data['operation']
#     else:
#         update.message.reply_text("Enter a valid command.")
#
# updater = telegram.ext.Updater(TOKEN, use_context=True)
#
# dispatch = updater.dispatcher
#
# dispatch.add_handler(telegram.ext.CommandHandler("start", start))
# dispatch.add_handler(telegram.ext.CommandHandler("timetable", timetable))
# dispatch.add_handler(telegram.ext.CommandHandler("sgpa", sgpa))
#
# dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_input))
#
# updater.start_polling()
# updater.idle()
def sum(num1,num2,num3):
    add=num1+num2+num3
    return add

def mul(num1,num2):
    ans=num1*num2
    return ans


#
# import telegram.ext
# import kiit
# import result
# import detail
#
# TOKEN = "6832286166:AAFlWnEY2fTKABtldlcWO18QJUddWlTB-z0"
#
# def start(update, context):
#     update.message.reply_text("Enter your choice. Select one of them:\n1. \timetable\n2. \sgpa .")
#
# def timetable(update, context):
#     update.message.reply_text("Enter your roll no:")
#     context.user_data['operation'] = 'timetable'
#
# def sgpa(update, context):
#     update.message.reply_text("Enter your roll no:")
#     context.user_data['operation'] = 'sgpa'
#
# def ask_roll_number(update, context):
#     user_input = update.message.text
#     context.user_data['roll_no'] = int(user_input)
#     # Initialize a list to store subject credits
#     context.user_data['subject_credits'] = []
#
#     # Ask the first question for subject credits
#     update.message.reply_text("Enter credits for the first subject:")
#
# def ask_total_credit(update, context):
#     user_input = update.message.text
#     context.user_data['total_credit'] = int(user_input)
#
# def handle_input(update, context):
#     user_input = update.message.text
#     operation = context.user_data.get('operation')
#
#     if operation == 'timetable':
#         s = detail.det(int(user_input))
#         update.message.reply_text(f"{s}")
#
#     elif operation == 'sgpa':
#         # Check if roll number is collected
#         if 'roll_no' not in context.user_data:
#             ask_roll_number(update, context)
#         # Check if total credit is collected
#         elif 'total_credit' not in context.user_data:
#             ask_total_credit(update, context)
#         else:
#             # Add the subject credits to the list
#             context.user_data['subject_credits'].append(float(user_input))
#
#             # Check if all questions have been asked
#             if len(context.user_data['subject_credits']) < 5:  # Assuming 5 subjects for example
#                 # Ask the next question
#                 update.message.reply_text(f"Enter credits for the next subject ({len(context.user_data['subject_credits']) + 1}):")
#             else:
#                 # Calculate SGPA and reply to the user
#                 total_credits = sum(context.user_data['subject_credits'])
#                 sgpa_result = result.res(context.user_data['total_credit'], total_credits)
#                 update.message.reply_text(f"Your SGPA: {sgpa_result}")
#
#                 # Clear user data
#                 del context.user_data['roll_no']
#                 del context.user_data['total_credit']
#                 del context.user_data['subject_credits']
#                 del context.user_data['operation']
#     else:
#         update.message.reply_text("Enter a valid command.")
#
# updater = telegram.ext.Updater(TOKEN, use_context=True)
#
# dispatch = updater.dispatcher
#
# dispatch.add_handler(telegram.ext.CommandHandler("start", start))
# dispatch.add_handler(telegram.ext.CommandHandler("timetable", timetable))
# dispatch.add_handler(telegram.ext.CommandHandler("sgpa", sgpa))
#
# dispatch.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text & ~telegram.ext.Filters.command, handle_input))
#
# updater.start_polling()
# updater.idle()





