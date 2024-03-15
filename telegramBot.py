from telegram import *
from telegram.ext import *
from asyncio import *

TOKEN = 'your toke here'

async def confirm_age(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Da", callback_data='yes'),
         InlineKeyboardButton("Nu", callback_data='no')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Confirmati ca aveti peste 18 ani?", reply_markup=reply_markup)

async def start_command(update: Update, context: CallbackContext):
    await confirm_age(update, context)

async def handle_age_confirmation(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'yes':
        keyboard = [
            [InlineKeyboardButton("Chat cu psiholog", callback_data='psychologist'),
            InlineKeyboardButton("Suport medical rapid", callback_data='emergency')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.edit_text("Bine ați venit în meniul principal!", reply_markup=reply_markup)
    elif query.data == 'no':
        await query.message.edit_text("Ne pare rău, nu puteți continua cu funcționalitatea botului.")

async def psychologist_button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'psychologist':
        query.edit_message_text(text="Alegeți categorie pentru întrebare:")
        
        numbers_keyboard = [
            [InlineKeyboardButton("====== Meniu principal ======", callback_data='principal')], 
            [InlineKeyboardButton("Serviciu de asistență în caz de viol", callback_data='serviciu asistenta')], 
            [InlineKeyboardButton("Trauma din copilărie", callback_data='copilarie')],
            [InlineKeyboardButton("Pierderea unei persoane apropiate", callback_data='pierderea persoanei')],
            [InlineKeyboardButton("Suport în urma unei experiențe nefericite", callback_data='nefericire')],
            [InlineKeyboardButton("Situații de stres cronic", callback_data='stres')],
            [InlineKeyboardButton("Învățare și transformare personală", callback_data='invatare')],
            [InlineKeyboardButton("Situații legate de folosirea drogurilor", callback_data='situatii droguri')]
        ]

        numbers_reply_markup = InlineKeyboardMarkup(numbers_keyboard)
        await query.message.reply_text("Alegeți categorie pentru întrebare:", reply_markup=numbers_reply_markup)

async def ajutor_medical(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'emergency':
        query.edit_message_text(text="12233")
        
        numbers_keyboard = [
            [InlineKeyboardButton("====== Meniu principal ======", callback_data='principal')],
            [InlineKeyboardButton("Cazuri de violență", callback_data='cazuri violenta')],
            [InlineKeyboardButton("Consum abuziv de droguri", callback_data='consum droguri')],
            [InlineKeyboardButton("Alte situații...", callback_data='12')]
        ]

        numbers_reply_markup = InlineKeyboardMarkup(numbers_keyboard)
        await query.message.reply_text("Alegeți categorie pentru întrebare:", reply_markup=numbers_reply_markup)

async def return_meniu(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'principal':
        query.edit_message_text(text="12234")
        numbers_keyboard = [
        [InlineKeyboardButton("Chat cu psiholog", callback_data='psychologist'),
        InlineKeyboardButton("Suport medical rapid", callback_data='emergency')]
    ]
    reply_markup = InlineKeyboardMarkup(numbers_keyboard)
    await query.message.reply_text("Bine ați venit în meniul principal!", reply_markup=reply_markup)


async def consum_abuziv_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'consum droguri':
        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        
        options_keyboard = [
            ["Închide conversația privată"]
        ]

        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Suport medical rapid \nTema: Consum abuziv de droguri\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)

async def cazuri_violenta_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    if query.data == 'cazuri violenta':
        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        
        options_keyboard = [
            ["Închide conversația privată"]
        ]

        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Suport medical rapid \nTema: Cazuri de violență\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)


async def serviciu_asistent_viol_callback(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()
    if query.data == 'serviciu asistenta':

        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        options_keyboard = [
            ["Închide conversația privată"]
        ]
        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Chat cu psiholog \nTema: Serviciu de asistență în caz de viol\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)


async def pierderea_persoanei_callback(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()
    if query.data == 'pierderea persoanei':

        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        options_keyboard = [
            ["Închide conversația privată"]
        ]
        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Chat cu psiholog \nTema: Pierderea unei persoane apropiate\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)


async def copilarie_callback(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()
    if query.data == 'copilarie':

        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        options_keyboard = [
            ["Închide conversația privată"]
        ]
        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Chat cu psiholog \nTema: Trauma din copilărie\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)

async def nefericire_callback(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()
    if query.data == 'nefericire':

        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        options_keyboard = [
            ["Închide conversația privată"]
        ]
        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Chat cu psiholog \nTema: Suport în urma unei experiențe nefericite\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)

async def stres_callback(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()
    if query.data == 'stres':

        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        options_keyboard = [
            ["Închide conversația privată"]
        ]
        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Chat cu psiholog \nTema: Situații de stres cronic\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)

async def invatare_callback(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()
    if query.data == 'invatare':

        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        options_keyboard = [
            ["Închide conversația privată"]
        ]
        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Chat cu psiholog \nTema: Învățare și transformare personală\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)

async def situatii_droguri_callback(update: Update, context: CallbackContext):

    query = update.callback_query
    query.answer()
    if query.data == 'situatii droguri':

        query.edit_message_text(text="Selectează opțiunea subsecțiunii 'Consum abuziv de droguri':")
        options_keyboard = [
            ["Închide conversația privată"]
        ]
        options_reply_markup = ReplyKeyboardMarkup(options_keyboard, resize_keyboard=True, one_time_keyboard=True)
        await query.message.reply_text("Tip: Chat cu psiholog \nTema: Situații legate de folosirea drogurilor\n ================================== \n \n Ești într-o conversație privata, cum te putem ajuta?", reply_markup=options_reply_markup)




def error(update: Update, context: CallbackContext):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting...')
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CallbackQueryHandler(handle_age_confirmation, pattern='yes|no'))
    # app.add_handler(CommandHandler('help', help_command))
    # app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CallbackQueryHandler(psychologist_button_callback, pattern='psychologist'))
    app.add_handler(CallbackQueryHandler(ajutor_medical, pattern='emergency'))
    app.add_handler(CallbackQueryHandler(return_meniu, pattern='principal'))


    app.add_handler(CallbackQueryHandler(consum_abuziv_callback, pattern='consum droguri'))
    app.add_handler(CallbackQueryHandler(cazuri_violenta_callback, pattern='cazuri violenta'))
    app.add_handler(CallbackQueryHandler(pierderea_persoanei_callback, pattern='pierderea persoanei'))

    app.add_handler(CallbackQueryHandler(serviciu_asistent_viol_callback, pattern='serviciu asistenta'))
    app.add_handler(CallbackQueryHandler(copilarie_callback, pattern='copilarie'))
    app.add_handler(CallbackQueryHandler(nefericire_callback, pattern='nefericire'))
    app.add_handler(CallbackQueryHandler(stres_callback, pattern='stres'))
    app.add_handler(CallbackQueryHandler(invatare_callback, pattern='invatare'))
    app.add_handler(CallbackQueryHandler(situatii_droguri_callback, pattern='situatii droguri'))

    app.add_error_handler(error)

    print('Polling ...')
    app.run_polling(poll_interval=3)
    gvh 
