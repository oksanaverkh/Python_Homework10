import logger as log    
from telegram import Update, Message
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext

new_list = []
result_fc = 0

async def start(update: Update, context: CallbackContext):
    await log.logger('User starts the program')
    await update.message.reply_text(f'''Choose an operation: 
        enter math task - enter /choose,
        logger journal unload - enter /load''')
    await log.logger('User chose an operation')
    user_input = update.message.text

async def choose(update: Update, context: CallbackContext):
    await log.logger('User choose numbers type')
    await update.message.reply_text(f'''Choose numbers type: 
        natural - enter /nat and enter math task without spaces,
        fractional or complex - enter /fc''')
    await log.logger('User chose numbers type')
    await log.log(update, context)
    user_input = update.message.text

async def get_data_natural(update: Update, context: CallbackContext):

    global new_list
    new_list = []
    text = update.message.text.split()[1]
    await update.message.reply_text('Enter /result')

    await log.logger(f'User entered math task')
    await log.log(update, context)
    num = ''
    if text[0]=='(':
        new_list.append(text[0])
        text = text[1:]
    for i, elem in enumerate(text):
        if elem.isdigit():
            num += elem
        elif elem in '()':
            if num !='': 
                new_list.append(int(num))
            new_list.append(elem)
            num=''
        else:
            if num !='':    
                new_list.append(int(num))
            new_list.append(elem)
            num=''
    if new_list[-1] != num and new_list[-1] != ')':
        new_list.append(int(num))

    i = 0
    while i<len(new_list):
        if new_list[i]=='(':
            index1 = new_list.index('(')
            index2 = new_list.index(')')
            new_list = new_list[:index1]+calc(new_list[index1+1:index2])+new_list[index2+1:]
        i+=1
    await log.logger('Calculation starts')

def calc(any_list):
    if '*' in any_list:
        i = 1
        while i<len(any_list):
            if any_list[i] =='*':
                result = any_list.pop(i+1)*any_list.pop(i-1)
                any_list[i-1] = result
                i=0
            i+=1

    if '/' in any_list:
        i = 1
        while i<len(any_list):
            if any_list[i] =='/':
                result = any_list[i-1]/any_list[i+1]
                any_list.pop(i+1)
                any_list.pop(i-1)
                any_list[i-1] = result
                i=0
            i+=1

    if '+' in any_list:
        i = 1
        while i<len(any_list):
            if any_list[i] =='+':
                result = any_list.pop(i+1)+any_list.pop(i-1)
                any_list[i-1] = result
                i=0
            i+=1

    if '-' in any_list:
        i = 1
        while i<len(any_list):
            if any_list[i] =='-':
                result = any_list[i-1]-any_list[i+1]
                any_list.pop(i+1)
                any_list.pop(i-1)
                any_list[i-1] = result
                i=0
            i+=1

    return any_list


async def get_result_natural(update: Update, context: CallbackContext):
    global new_list
    await log.logger(f'Calculation starts')
    res = calc((new_list))[0]
    await update.message.reply_text(f'Result = {res}')
    await log.logger(f'Result displayed to user')
    await log.log(update, context)


async def get_data_fc(update: Update, context: CallbackContext):
    await update.message.reply_text('Enter number 1 + space:')
    await update.message.reply_text('Enter an operator + space:')
    await update.message.reply_text('Enter number 2:')
    await update.message.reply_text('Enter /resfc')
    text = update.message.text.split()
    a = text[1]
    op = text[2]
    b = text[3]
    await log.logger(f'User entered numbers and operator')
    await log.log(update, context)

    if 'j' in a or 'j' in b:
        if 'j' in a:
            a = complex(a)
        if 'j' in b:
            b = complex(b)
    elif '.' in a or '.' in b:
        if '.' in a:
            a = float(a)
        if '.' in b:
            b = float(b)

    global result_fc
    result_fc = 0
    await log.logger(f'Calculation in progress {a} {op} {b}')
    if op == '+':
        result_fc = a+b
    elif op == '-':
        result_fc = a-b
    elif op == '*':
        result_fc = a*b
    elif op == '/':
        result_fc = a/b



async def get_result_fc(update: Update, context: CallbackContext):
    global result_fc
    await update.message.reply_text(f'Result = {result_fc}')
    await log.logger(f'Result displayed to user {result_fc}')
    await log.logger(f'Result displayed to user')
    await log.log(update, context)


