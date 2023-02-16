from telebot.async_telebot import AsyncTeleBot
import asyncio
from GPT_generator import generate_GPT
from utils import * 

TOKEN = read_config()["telegram_token"]

bot = AsyncTeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
async def send_welcome(message):
	await bot.send_message(message.chat.id, "Hello, to start using... just write and GPT model will answer")

@bot.message_handler(func=lambda message: True)
async def echo_all(message):
	await bot.send_message(message.chat.id, generate_GPT(message.text))


asyncio.run(bot.infinity_polling())