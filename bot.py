import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)

items = {
  'btn1' : ('Пластиковая бутылка', '450 лет'),
  'btn2' : ('Кожура банана', 'до двух лет'),
  'btn3' : ('Стекло', 'более 1000 лет'),
  'btn4' : ('Полиэтиленовый пакет', 'от 5 до 10 лет'),
  'btn5' : ('Бумага', '2 года')
}


def get_inline_keyboard():
  markup = InlineKeyboardMarkup()
  markup.add(InlineKeyboardButton('Пластиковая бутылка', callback_data='btn1'))
  markup.add(InlineKeyboardButton('Кожура банана', callback_data='btn2'))
  markup.add(InlineKeyboardButton('Стекло', callback_data='btn3'))
  markup.add(InlineKeyboardButton('Полиэтиленовый пакет', callback_data='btn4'))
  markup.add(InlineKeyboardButton('Бумага', callback_data='btn5'))
  return markup

@bot.message_handler(commands=['start', 'help'])
def starting(message):
  bot.send_message(message.chat.id, 'Привет! Я Эко-Бот Напиши команду /eco')

@bot.message_handler(commands=['eco'])
def eco_items(message):
  bot.send_message(message.chat.id, 'Выбери предмет, для которого хочешь узнать сколько он разлогается', reply_markup=get_inline_keyboard())

@bot.callback_query_handler(func=lambda call: call.data in ['btn1', 'btn2', 'btn3', 'btn4', 'btn5'])
def handle_inline_keyboard(call):
  name, items_Decomposition_time = items[call.data]
  bot.answer_callback_query(call.id)
  bot.send_message(call.message.chat.id, f'{name} {items_Decomposition_time}')

bot.infinity_polling()
