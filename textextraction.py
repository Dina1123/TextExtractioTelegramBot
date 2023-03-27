
import telegram
from telegram.ext import Updater, MessageHandler
from telegram.ext import Filters
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define a function to handle incoming messages
def handle_message(update, context):
    # Get the image from the message
    photo_file = update.message.photo[-1].get_file()
    image_path = 'image.jpg'
    photo_file.download(image_path)
    image = Image.open(image_path)
    
    

    text = pytesseract.image_to_string(image, lang='eng',  config='--psm 11 --oem 1')
   
    if text:
        response_text = "Here is the text I extracted: " + text
    else:
        response_text = "Sorry, I couldn't recognize any text in the image."

    context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)
    
 
updater = Updater('6080419832:AAEPGEXdz_YDF-DliSnDRSCClUa8zzghWQM')
message_handler = MessageHandler(Filters.photo, handle_message)

updater.dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
