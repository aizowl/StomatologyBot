import telegram
from kb import tele_buttons, stomat_menu


 
def main_menu_keyboard():

    keyboard=([
        [
            telegram.KeyboardButton(tele_buttons[0]),
            telegram.KeyboardButton(tele_buttons[1]),
            telegram.KeyboardButton(tele_buttons[2]),
            telegram.KeyboardButton(tele_buttons[3]),
        ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False

    )


def stomat_menu_keyboard():

    keyboard=([
        [
            telegram.KeyboardButton(stomat_menu[0]),
            telegram.KeyboardButton(stomat_menu[1]),
            telegram.KeyboardButton(stomat_menu[2]),
            telegram.KeyboardButton(stomat_menu[3]),
            
        ]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False

    )
