# -*- coding: utf8 -*-
import random

import telebot
from telebot import types

bot = telebot.TeleBot('1309778419:AAEW5DbXKeLVTH01mxQEvpY2d5I1gmtRuEg');


@bot.message_handler(commands=['start'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id,
                         "Привет! \nНапиши /help, чтобы узнать информацию о боте");


@bot.message_handler(commands=['info'])
def help(message):
    if message.text == '/info':
        bot.send_photo(message.chat.id, 'https://pbs.twimg.com/media/EHagwVQUUAEsRxM.jpg', 'Нippie Sabotage — американская группа, участниками которой стали братья Кевин и Джефф Сауреры. Парни начали заниматься музыкой в детстве. К 2019 году за их плечами оказались альбомы, клипы и треки, ставшие хитами. Дуэт регулярно дает концерты и становится приглашенным гостем европейских и американских фестивалей.')

@bot.message_handler(commands=['now'])
def help(message):
    if message.text == '/now':
        bot.send_photo(message.chat.id, 'https://avatars.mds.yandex.net/get-zen_doc/151305/pub_5d79129295aa9f3dea0a5627_5d8fd65d6f5f6f00b0f9da8e/scale_1200', 'Состав дуэта с момента его основания оставался неизменным, и творческий вектор, однажды выбранный музыкантами, стал своеобразной константой. Сегодня Кевин и Джефф выглядят как настоящие хиппи. Они носят самую незамысловатую одежду, отдают предпочтение длинным волосам и демонстративно фотографируются с самокрутками. \nСейчас у артистов есть официальный сайт, а также аккаунты в социальных сетях, где они делятся фото, промоматериалами и планом концертов')
@bot.message_handler(commands=['history'])
def help(message):
    if message.text == '/history':
        bot.send_photo(message.chat.id, 'http://www.youngcalifornia.com/wp-content/uploads/2018/10/38839691_2238202556498369_6300129188238065664_n.jpg', 'Что их биография будет связана с творчеством, Сауреры поняли в 12 лет. В этом возрасте мальчики из Сакраменто начали записывать свои первые композиции. Среди всех направлений в музыке наиболее близким братьям показался хип-хоп'
        '\nТак стартовала история создания коллектива. В 2008-м Кевину и Джеффу предложил сотрудничество продюсер Чейз Мур. Спустя некоторое время музыканты начали взаимодействовать с представителями хип-хоп-сообщества из Чикаго. Среди партнеров исполнителей оказывались разные артисты, в том числе J. Leake и Yukmouth, Calez и Kami de Chukwu и другие.')
        bot.send_photo(message.chat.id,'https://media1.fdncms.com/saltlake/imager/u/original/13988118/hippie_sabotage_-_pc_marlowe_teichman.jpg',
        'Артисты демонстрировали творческий рост. Их треки становились не просто набором битов, звучание обретало многогранность. Братья начали создавать музыку для рэперов Alex Wiley и C Plus. В 2013-м состоялась премьера их авторского альбома. Парни объединили собственный материал в пластинке Vacants. В том же году были презентованы синглы White Tiger и Sunny.'
         '\nАудитория музыкантов оставалась скромной до тех пор, пока исполнительница Элли Голдинг не поделилась ремиксом песни Stay High с фолловерами в «Инстаграме». Нippie Sabotage поработали с композицией шведской певицы Tove Lo. Их ремикс оказался в самых популярных музыкальных чартах. Так исполнители привлекли к себе внимание профессионального сообщества и публики. Ролик набрал более 1 млн прослушиваний, а лестный комментарий обладательницы аккаунта сыграл братьям на руку.')
        bot.send_photo(message.chat.id,'https://www.melodicmag.com/wp-content/uploads/2018/06/music_hippie_sabotage_handout.5a46a502f1dce.jpg',
       'Композиции артистов одна за другой становились хитами. Ремикс трека Habits, опубликованный на «Ютьюбе», собрал больше 700 млн просмотров. Нippie Sabotage начали работу над новыми альбомами. В 2014-м они презентовали пластинки Johnny Long Chord и The Sunny Album. Диски сочетали инструментальную музыку, хип-хоп и элементы других жанров.')

@bot.message_handler(commands=['help'])
def help(message):
    if message.text == '/help':
        bot.send_message(message.from_user.id, "Я музыкальный бот, который поможет тебе скачать треки гурппы 'Hippie Sabotage' \nНапиши /choose, чтобы выбрать трек \n/info - чтобы узнать основную ифнормацию о группе \n/history - чтобы узнать историю создания  \n/now - чтобы узнать, что с группой сейчас");

@bot.message_handler(commands=['choose'])
def start(message):
    if message.text == "/choose":
        keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard.row('Providence','The Sunny Album','Drifter')
        bot.send_message(message.from_user.id, 'Для начала выбери нужный альбом!', reply_markup=keyboard)
        bot.register_next_step_handler(message, choose);
    else:
        bot.send_message(message.from_user.id, 'Я не понимаю. Напиши /help.');

@bot.message_handler(content_types=['text'])
def choose(message):
    if message.text == 'Providence':
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text='Glimpse', callback_data='Glimpse')
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Please Understand', callback_data='Please Understand')
        keyboard.add(key2)
        key3 = types.InlineKeyboardButton(text='Devil Eyes', callback_data='Devil Eyes')
        keyboard.add(key3)
        key4 = types.InlineKeyboardButton(text='Hidden Places', callback_data='Hidden Places')
        keyboard.add(key4)
        key5 = types.InlineKeyboardButton(text='Waiting', callback_data='Waiting')
        keyboard.add(key5)
        key6 = types.InlineKeyboardButton(text='Not Enough', callback_data='Not Enough')
        keyboard.add(key6)
        key7 = types.InlineKeyboardButton(text='Feeling Crazy', callback_data='Feeling Crazy')
        keyboard.add(key7)
        key8 = types.InlineKeyboardButton(text='Gold', callback_data='Gold')
        keyboard.add(key8)
        bot.send_message(message.from_user.id, text='Выберите трек', reply_markup=keyboard)
    elif message.text == 'The Sunny Album':
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text="Don't Leave Me Alone", callback_data="Don't Leave Me Alone")
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Go To Work', callback_data='Go To Work')
        keyboard.add(key2)
        key3 = types.InlineKeyboardButton(text='Take Over', callback_data='Take Over')
        keyboard.add(key3)
        key4 = types.InlineKeyboardButton(text='The Wave', callback_data='The Wave')
        keyboard.add(key4)
        key5 = types.InlineKeyboardButton(text='In Your Eyes', callback_data='In Your Eyes')
        keyboard.add(key5)
        key6 = types.InlineKeyboardButton(text='Moving Time', callback_data='Moving Time')
        keyboard.add(key6)
        key7 = types.InlineKeyboardButton(text='On and On', callback_data='On and On')
        keyboard.add(key7)
        key8 = types.InlineKeyboardButton(text='Picture This', callback_data='Picture This')
        keyboard.add(key8)
        key9 = types.InlineKeyboardButton(text='Smoking Room', callback_data='Smoking Room')
        keyboard.add(key9)
        bot.send_message(message.from_user.id, text='Выберите трек', reply_markup=keyboard)
    elif message.text == 'Drifter':
        keyboard = types.InlineKeyboardMarkup()
        key1 = types.InlineKeyboardButton(text="Peyote", callback_data="Peyote")
        keyboard.add(key1)
        key2 = types.InlineKeyboardButton(text='Angels on My Side', callback_data='Angels on My Side')
        keyboard.add(key2)
        key3 = types.InlineKeyboardButton(text='Om', callback_data='Om')
        keyboard.add(key3)
        key4 = types.InlineKeyboardButton(text='Otherside', callback_data='Otherside')
        keyboard.add(key4)
        key5 = types.InlineKeyboardButton(text='Lights Out', callback_data='Lights Out')
        keyboard.add(key5)
        key6 = types.InlineKeyboardButton(text='Bob Dylan', callback_data='Bob Dylan')
        keyboard.add(key6)
        bot.send_message(message.from_user.id, text='Выберите трек', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Я не понимаю. Напиши /help.');

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Please Understand":
        bot.send_audio(call.message.chat.id, 'https://w1.musify.club/track/dl/6081195/hippie-sabotage-please-understand.mp3')
    elif call.data == "Devil Eyes":
        bot.send_audio(call.message.chat.id,'https://rum.zvukofon.com/dl/465300272/Hippie_Sabotage_-_Devil_Eyes_(musicport.org).mp3')
    elif call.data == "Hidden Places":
        bot.send_audio(call.message.chat.id, 'https://w1.musify.club/track/dl/6081200/hippie-sabotage-hidden-places.mp3')
    elif call.data == "Glimpse":
        bot.send_audio(call.message.chat.id, 'https://w1.musify.club/track/dl/6081194/hippie-sabotage-glimpse.mp3')
    elif call.data == "Waiting":
        bot.send_audio(call.message.chat.id,'https://rum.zvukofon.com/dl/1031525719/Hippie_Sabotage_-_Waiting_(musicport.org).mp3')
    elif call.data == "Not Enough":
        bot.send_audio(call.message.chat.id, 'https://w1.musify.club/track/dl/6081201/hippie-sabotage-not-enough.mp3')
    elif call.data == "Feeling Crazy":
        bot.send_audio(call.message.chat.id,'https://w1.musify.club/track/dl/6081202/hippie-sabotage-feeling-crazy.mp3')
    elif call.data == "Gold":
        bot.send_audio(call.message.chat.id,'https://w1.musify.club/track/dl/6081196/hippie-sabotage-gold.mp3')
    elif call.data == "Smoking Room":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1413369044/Hippie_Sabotage_-_Smoking_Room_(musicport.org).mp3')
    elif call.data == "Picture This":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1484389689/Hippie_Sabotage_-_Picture_This_(musicport.org).mp3')
    elif call.data == "On and On":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1899620184/Hippie_Sabotage_-_On_and_On_(musicport.org).mp3')
    elif call.data == "Moving Time":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/721011071/Hippie_Sabotage_-_Moving_Time_(musicport.org).mp3')
    elif call.data == "In Your Eyes":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1136241566/Hippie_Sabotage_-_In_Your_Eyes_(musicport.org).mp3')
    elif call.data == "The Wave":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/377408049/Hippie_Sabotage_-_The_Wave_(musicport.org).mp3')
    elif call.data == "Don't Leave Me Alone":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1756971554/Hippie_Sabotage_-_Dont_Leave_Me_Alone_(musicport.org).mp3')
    elif call.data == "Go To Work":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1702467005/Hippie_Sabotage_-_Go_to_Work_(musicport.org).mp3')
    elif call.data == "Bob Dylan":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1143630421/Hippie_Sabotage_-_Bob_Dylan_(musicport.org).mp3')
    elif call.data == "Lights Out":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/107669938/Hippie_Sabotage_-_Lights_Out_(musicport.org).mp3')
    elif call.data == "Otherside":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1273701740/Hippie_Sabotage_-_Otherside_(musicport.org).mp3')
    elif call.data == "Om":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1965793481/Hippie_Sabotage_-_Om_(musicport.org).mp3')
    elif call.data == "Angels on My Side":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/32240228/Hippie_Sabotage_-_Angels_on_My_Side_(musicport.org).mp3')
    elif call.data == "Peyote":
        bot.send_audio(call.message.chat.id, 'https://rum.zvukofon.com/dl/1920289730/Hippie_Sabotage_-_Peyote_(musicport.org).mp3')


bot.polling()
