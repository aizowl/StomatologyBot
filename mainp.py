import re
from telegram import (Update, InlineKeyboardButton, InlineKeyboardMarkup, chat, keyboardbutton,
 replymarkup, )

from telegram.callbackquery import CallbackQuery
from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler, 
    PicklePersistence,
    Filters,
    MessageHandler,
    CallbackQueryHandler
)
from telegram.messageentity import MessageEntity
from menup import stomat_menu_keyboard, main_menu_keyboard
from cr import TOKEN
from kb import tele_buttons, stomat_menu
from message import text1, text2




def start(update: Update, context:CallbackContext):
    update.message.reply_text(
        'Здравствуйте, {username}!Чтобы подробнее узнать о нашей стоматологии,пройдите в меню. Чтобы записаться нажмите на кнопку "Записаться": '.format(
        username=update.effective_user.first_name \
            if update.effective_user.first_name is not None \
            else update.effective_user.username
        ), 
        reply_markup=main_menu_keyboard()
    )

ADRES_REGEX =r'(?=('+(tele_buttons[2])+r'))'
ZAPIS_REGEX =r'(?=('+(tele_buttons[3])+r'))'
USLUGI_REGEX =r'(?=('+(tele_buttons[0])+r'))'
STOMAT_REGEX =r'(?=('+(tele_buttons[1])+r'))'
KA_REGEX =r'(?=('+(stomat_menu[1])+r'))'
AA_REGEX =r'(?=('+(stomat_menu[1])+r'))'   
BJ_REGEX =r'(?=('+(stomat_menu[1])+r'))'
AK_REGEX =r'(?=('+(stomat_menu[1])+r'))'

def zapisat(update: Update, context:CallbackContext):
    z = update.message.text
    print(z[:6])
    if z[:6] == 'Запись':
        context.bot.send_message(
            chat_id = '@aident_stom', 
            text = z
        )

def uslugi(update: Update, context: CallbackContext):
    info=re.match(USLUGI_REGEX, update.message.text)
    update.message.reply_text(
        text1
    )

def zapis(update: Update, context: CallbackContext):
    info=re.match(USLUGI_REGEX, update.message.text)
    update.message.reply_text(
        text2
    )
def adres(update: Update, context: CallbackContext):
    info=re.match(ADRES_REGEX, update.message.text)
    update.message.reply_location(
        longitude=74.58321910950968,
        latitude=42.870713323734364
    )

def ka_menu():
    keyboard = [
    [InlineKeyboardButton("Его работы", callback_data='ka_raboty')],
    [InlineKeyboardButton("Фото", callback_data='ka_photo')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup
def aa_menu():
    keyboard = [
    [InlineKeyboardButton("Ее работы", callback_data='aa_raboty')],
    [InlineKeyboardButton("Фото", callback_data='aa_photo')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup
def bj_menu():
    keyboard = [
    [InlineKeyboardButton("Его работы", callback_data='bj_raboty')],
    [InlineKeyboardButton("Фото", callback_data='bj_photo')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup
def ak_menu():
    keyboard = [
    [InlineKeyboardButton("Ее работы", callback_data='ak_raboty')],
    [InlineKeyboardButton("Фото", callback_data='ak_photo')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    return reply_markup


def receive_stomat_menu(update: Update, context: CallbackContext):
    info=re.match(STOMAT_REGEX, update.message.text)
    keyboard = [
    [InlineKeyboardButton("Кайрат Азимбаевич", callback_data='st1')],
    [InlineKeyboardButton("Алена Александровна", callback_data='st2')],
    [InlineKeyboardButton("Бекболот Женишбекович", callback_data='st3')],
    [InlineKeyboardButton("Аида Кубанычбековна", callback_data='st4')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Выберите Стоматолога для просмотра информации о нем', 
        reply_markup=reply_markup
    )

def inline_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'st1':
        query.message.reply_text(
            text='''
Кайрат Азимбаевич стоматолог высшего ранга с опытом работы в более чем 5 лет. Высоко-квалифицированный
специалист в своем деле. Диплом от выш.мед.учреждения Турции им.Кашгари.
Основатель AiDentalClinic''',
            reply_markup=ka_menu()
            )
    if query.data == 'st2':
        query.message.reply_text(
            text='''
Алена Александрона стоматолог-травматолог высшего ранга с опытом работы в более чем 12 лет. Высоко-квалифицированный
специалист в своем деле. Диплом от выш.мед.учреждения КГМА.''',
            reply_markup=aa_menu()
)
    if query.data == 'st3':
        query.message.reply_text(
            text='''
Бекболот Женишбекович стоматолог-косметолог высшего ранга с опытом работы в более чем 10 лет. Высоко-квалифицированный
специалист в своем деле. Диплом от выш.мед.учреждения Турции им.Кашгари.''',
            reply_markup=bj_menu()
)
    if query.data == 'st4':
        query.message.reply_text(
            text='''
Аида Кубанычбековна стоматолог-диетист высшего ранга с опытом работы в более чем 12 лет. Высоко-квалифицированный
специалист в своем деле. Диплом от выш.мед.учреждения КГМА.''',
            reply_markup=ak_menu()
)
    if query.data == 'ka_photo':
        query.message.reply_text(
            text='https://bydent.kg/wp-content/uploads/2020/06/16.jpg',
            reply_markup=ka_menu()
)
    if query.data == 'ka_raboty':
        query.message.reply_text(
            text='https://www.womanhit.ru/media/CACHE/images/articleimage2/2017/6/4_zySYHwB/567a1fce2777b79b84c6222ceca0a356.png',
            reply_markup=ka_menu()
)
    if query.data == 'aa_photo':
        query.message.reply_text(
            text='https://bydent.kg/wp-content/uploads/job-manager-uploads/person_photo/2019/12/alena1.jpeg',
            reply_markup=aa_menu()
)
    if query.data == 'aa_raboty':
        query.message.reply_text(
            text='https://www.clinikadoctordent.ru/upload/resize_cache/iblock/a55/329_235_2/a5582c5752c17d22c995808bbab35e2c.webp',
            reply_markup=aa_menu()
)
    if query.data == 'bj_photo':
        query.message.reply_text(
            text='https://bydent.kg/wp-content/uploads/job-manager-uploads/person_photo/2020/12/13-rus1.jpg',
            reply_markup=bj_menu()
)
    if query.data == 'bj_raboty':
        query.message.reply_text(
            text='http://service-med.com/wp-content/uploads/operation-jaw.jpg',
            reply_markup=bj_menu()
)
    if query.data == 'ak_photo':
        query.message.reply_text(
            text='https://bydent.kg/wp-content/uploads/job-manager-uploads/person_photo/2020/07/aida2.jpg',
            reply_markup=ak_menu()
)
    if query.data == 'ak_raboty':
        query.message.reply_text(
            text='https://avatars.mds.yandex.net/get-zen_doc/2424254/pub_5ea9602b87ea957abad0dbd4_5ea96159d1cbcf0a0cd0b9e9/scale_1200',
            reply_markup=ak_menu()
)

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(STOMAT_REGEX), 
    receive_stomat_menu
))





updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(USLUGI_REGEX), 
    uslugi
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAPIS_REGEX), 
    zapis
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ADRES_REGEX), 
    adres
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text, 
    zapisat
))
updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))

updater.start_polling()
updater.idle()