# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

import logger as log
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import bot_commands as bc

import os
os.system('cls')

app = ApplicationBuilder().token("YOUR TOKEN").build()
print('server start')
     
app.add_handler(CommandHandler("start", bc.start))
app.add_handler(CommandHandler("choose", bc.choose))
app.add_handler(CommandHandler("nat", bc.get_data_natural))
app.add_handler(CommandHandler("result", bc.get_result_natural))
app.add_handler(CommandHandler("fc", bc.get_data_fc))
app.add_handler(CommandHandler("resfc", bc.get_result_fc))

app.add_handler(CommandHandler("load", log.export_logging_journal))
app.add_handler(CommandHandler("txt", log.export_logging_journal_txt))
app.add_handler(CommandHandler("message", log.export_logging_journal_message))

app.run_polling()









