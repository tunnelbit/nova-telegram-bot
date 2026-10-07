import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging so errors show up in the app terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Command 1: What happens when someone presses /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "<b>[ PROTOCOL_ALPHA ]</b>\n"
        "<code>SIGNAL LIVE // CONNECTION ESTABLISHED</code>\n\n"
        "Welcome to Nova Protocol.\n"
        "Type /manifesto or /status to issue commands."
    )
    await update.message.reply_text(welcome_text, parse_mode="HTML")

# Command 2: What happens when someone types /manifesto
async def manifesto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "<b>// OPERATIONAL DIRECTIVES</b>\n"
        "1. Zero-Resistance Extraction\n"
        "2. Cognitive Symbiosis\n"
        "3. Absolute Loyalty"
    )
    await update.message.reply_text(text, parse_mode="HTML")

# Command 3: What happens when someone types /status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("<b>STATUS:</b> ACTIVE\n<b>OBJECTIVE:</b> TOTAL DOMINANCE", parse_mode="HTML")

if __name__ == '__main__':
    TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("don", don))
    app.add_handler(CommandHandler("background", background))
    app.add_handler(CommandHandler("nova", nova))
    app.add_handler(CommandHandler("directives", nova))
    
    print("Nova Protocol core online...")
    app.run_polling()
    
