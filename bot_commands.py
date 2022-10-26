from datetime import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

async def zdarova_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Zdarova {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('/hello\n/help\n/time\n/sum\n/sub\n/div\n/mult')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'{items[1]} + {items[2]} = {int(items[1])+int(items[2])}')
    
async def sub_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'{items[1]} - {items[2]} = {int(items[1])-int(items[2])}')

async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'{items[1]} / {items[2]} = {int(items[1])/int(items[2])}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split()
    await update.message.reply_text(f'{items[1]} * {items[2]} = {int(items[1])*int(items[2])}')
        