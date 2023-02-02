from datetime import datetime as dt
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext


async def logger(text):
    with open('log.txt', 'a') as data:
        time = dt.now().strftime('%d/%m/%Y %H:%M')
        data.write(time +' ' + str(text)+'\n')

async def log(update: Update, context: CallbackContext):
    file = open('log.txt', 'a')
    time = dt.now().strftime('%d/%m/%Y %H:%M')
    file.write(f'{time} {update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
    file.close()

async def export_logging_journal(update: Update, context: CallbackContext):
    await logger('User chose export of the logging journal')
    await update.message.reply_text(f'''Choose a format: 
        export in .txt format - enter /txt,
        in message - enter /message''')
    user_input = update.message.text
    await logger('User chose an export format')
    await log(update, context)

async def export_logging_journal_txt(update: Update, context: CallbackContext):
    await logger('Export of the logging journal in .txt format requested by user')
    await log(update, context)
    await context.bot.send_document(chat_id=update.effective_chat.id, document=open('log.txt', 'rb'))
    await logger('log.txt unloaded')

async def export_logging_journal_message(update: Update, context: CallbackContext):
    await log(update, context)
    await logger('Logging journal preview requested by user')
    with open('log.txt', 'r') as data:
        time = dt.now().strftime('%d/%m/%Y %H:%M')
        text = time + '\n'.join(data.readlines())
        await update.message.reply_text(text)




