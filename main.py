from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5560335758:AAEigha5GaE4dAxq6Ne03vorjpJSlpzCSwI").build()

app.add_handler(CommandHandler("hi", zdarova_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("mult", mult_command))

print('server start')
app.run_polling()