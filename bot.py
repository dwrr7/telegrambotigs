from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, filters, MessageHandler
import re
import random



key_token = "6910200818:AAF8gzYxdr5stYR6WyvgoxqrDz4MaK29g8c" #Masukkan KEY-TOKEN BOT 
user_bot = "HendiBot" #Masukkan @user bot


async def  start_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /help untuk menampilkan apa yang dapat saya berikan..")
    
async def  help_command(update: Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Kirim pesan, bot akan membalas pesan..")


async def  text_massage(update: Update, context:ContextTypes.DEFAULT_TYPE):
    text_diterima : str = update.message.text
    print(f"Pesan diterima : {text_diterima}")
    text_lwr_diterima = text_diterima.lower()
    if 'halo' in text_lwr_diterima:
        await update.message.reply_text("Hallo juga")
    elif 'selamat malam' in text_lwr_diterima:
        await update.message.reply_text("Selamat malam..., jangan lupa istirahat 😊")
    elif 'siapa kamu ?' in text_lwr_diterima:
        await update.message.reply_text(f"bot adalah : {user_bot}")
    elif 'hitung' in text_lwr_diterima:
        # Extracting numbers and operator from the message using regular expression
        match = re.match(r'hitung (\d+) ([+\-*/]) (\d+)', text_lwr_diterima)
        if match:
            num1 = int(match.group(1))
            operator = match.group(2)
            num2 = int(match.group(3))

            # Performing the calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero"
            else:
                result = "Error: Invalid operator"

            await update.message.reply_text(f"Hasil perhitungan: {result}")
        else:
            await update.message.reply_text("Format perintah hitung salah. Contoh: hitung 5 + 3")
    elif 'pilih angka' in text_lwr_diterima:
        # Extract the range from the message using regular expression
        match = re.match(r'pilih angka (\d+) - (\d+)', text_lwr_diterima)
        if match:
            range_start = int(match.group(1))
            range_end = int(match.group(2))

            # Generate a random integer within the specified range
            random_number = random.randint(range_start, range_end)

            await update.message.reply_text(f"Angka random antara {range_start} dan {range_end}: {random_number}")
        else:
            await update.message.reply_text("Format perintah pilih angka salah. Contoh: pilih angka 1 - 10")        
    
    else:
        await update.message.reply_text("bot tidak mengerti")


async def photo_message(update: Update, context:ContextTypes.DEFAULT_TYPE):
    return await update.message.reply_text("Gambar kamu bagus")
        
async def  error(update: Update, context:ContextTypes.DEFAULT_TYPE):
    print(f"error... : {context.error}")


if __name__ == '__main__':
    print("Mulai")
    app = Application.builder().token(key_token).build()
    #COMMAND :
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    #MESSAGE:
    app.add_handler(MessageHandler(filters.TEXT, text_massage))
    app.add_handler(MessageHandler(filters.PHOTO, photo_message))
    #error :
    app.add_error_handler(error)
    #polling :
    app.run_polling(poll_interval=1)




