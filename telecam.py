#!/usr/bin/python3.7

import telegram.ext
import logging
import picamera

logging.basicConfig(level=logging.DEBUG)

BOT_KEY = '1182296187:AAE00CpQ8krO42RZv_asrHUznZ8r8u_k3NE'
BOT_CHAT_ID = '63620166'
IMAGE_PATH = '/home/pi/Michael/image.jpg'
IMAGE_ROTATION = 270

def handle_start(bot, update):
    update.message.reply_text("yeah boiii")

def handle_picture(bot, update):
    bot.camera.capture(IMAGE_PATH)
    # cannot pass file path, have to pass stream
    update.message.reply_photo(open(IMAGE_PATH, 'rb'))

def setup_camera():
    camera = picamera.PiCamera()
    camera.rotation = IMAGE_ROTATION
    camera.start_preview()
    return camera

def setup_telegram():
    updater = telegram.ext.Updater(BOT_KEY)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(telegram.ext.CommandHandler("start", handle_start))
    dispatcher.add_handler(telegram.ext.CommandHandler("picture", handle_picture))
    return updater

def main():
    camera = setup_camera()
    updater = setup_telegram()
    updater.bot.camera = camera

    updater.start_polling()

if __name__ == '__main__':
    main()
