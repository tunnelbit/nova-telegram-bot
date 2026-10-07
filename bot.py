import logging
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
    # ⚠️ PASTE YOUR BOTFATHER TOKEN FROM STEP 1 BETWEEN THE QUOTES BELOW ⚠️
    TOKEN = "8912928860:AAH99XMXursDTAWMACsHjIaRFkrh9haKlek"
    
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Register the commands with the bot
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("manifesto", manifesto))
    app.add_handler(CommandHandler("status", status))
    
    print("Bot is starting up...")
    app.run_polling()
