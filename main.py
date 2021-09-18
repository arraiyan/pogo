from telegram import *
from telegram.ext import *
from inf import env
import init
import time
import re
import requests 
def is_admin(update:Update,context:CallbackContext)->None:
    if not update.message.chat.type == 'private':
        is_admin = False
        CurrentMemberData = context.bot.get_chat_member(chat_id=update.message.chat.id,user_id = update.message.from_user.id).to_dict()
        print(CurrentMemberData)
        if CurrentMemberData['status']=='administrator' or CurrentMemberData['status']=='creator':
            is_admin = True
        else:
            is_admin = False

        return is_admin 
    else:
        return True

def delete_command(update:Update,context:CallbackContext)->None:
    result = False
    if is_admin(update,context):
        result = True
    else:
        context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)
    return result




def dashboard(update:Update,context:CallbackContext):
    chat_id = update.message.chat.id
    if chat_id in env.logged_user:
        reply_markup = InlineKeyboardMarkup([[
            InlineKeyboardButton("Search by name", callback_data="search_name"),
            InlineKeyboardButton("Search by function", callback_data="search_function")]])

        context.bot.send_message(update.message.chat.id, "Please select:", reply_to_message_id = update.message.message_id,
                    reply_markup = env.dash_keys)
    else:
        update.message.reply_text('Login in first type in /login')












def invite_link(update:Update,context:CallbackContext)->None:
    if delete_command(update,context):
        data = requests.get(f'https://api.telegram.org/bot{env.API_KEY}/exportchatinvitelink?chat_id={update.message.chat.id}').json()
        link = data['result']
        print(link)
        context.bot.send_message(chat_id = update.message.chat.id ,text = link)
    return

def files(update:Update,context:CallbackContext)->None:
    print('al ac')
    if not delete_command(update,context):
        context.bot.send_message(chat_id = update.message.chat.id,text = env.file_text,parse_mode='HTML')
    return




def start(update: Update, context: CallbackContext) -> None:

    
    if update.message.chat.type == 'private':
        context.bot.send_message(chat_id = update.message.chat.id,text='PLease login using /login')
        return          
def ban(update:Update,context:CallbackContext)->None:
    if is_admin(update,context):
        echo = update.message.text_html
        
        print(f'{echo[5:len(echo)]}...')

        l = list(map(int, re.findall(r'\d+', str(echo))))# extracts numbers
        if not len(l)<=0:
            print('ir')
            context.bot.kick_chat_member(update.message.chat.id,user_id=int(l[0]),revoke_messages=True)
        else:
            print(env.user_trace)
            print('er')
            for i,j in env.user_trace.items():
                print(i)
                print(j)
                print(f'{echo[5:len(echo)]}')
                if str(i) == str(echo[5:len(echo)]):
                    print('pr')
                    context.bot.kick_chat_member(update.message.chat.id,user_id=int(j),revoke_messages=True)
                    return
            




    return


def login(update:Update,context:CallbackContext):
    chat_id = update.message.chat.id
    if update.message.chat.type == 'private':
        if not chat_id in env.logged_user:
            update.message.reply_text('PLEASE enter the password')
            env.method = 'login'
            return

        else:
            update.message.reply_text('you are already logged in enter /dash to open admin panel')

    

    return








# /invite generate one time invitation link
# /site The website address of pogo swap
# /airdrop all about airdrop
# /contact contact info
# /price value of pogoSwap
# /ban /ban @user_name will be banned
# /login login to dashboard (admin only ) private
# /dash dashboard (admin only) private
# /start (admin only) private
# /help



def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("/invite generate one time invitation link\n/site The website address of pogo swap\n/airdrop all about airdrop\n/contact contact info\n/price value of pogoSwap\n/ban /ban @user_name will be banned\n/login login to dashboard (admin only ) private\n/dash dashboard (admin only) private\n/start (admin only) private\n/help if user stucks")
    return

def new_member(update:Update, context:CallbackContext)->None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr' {env.welcome_message} ',
        reply_markup=ForceReply(selective=True),
    )


def left_member(update:Update, context:CallbackContext)->None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr' {env.lef_message} {user.mention_markdown_v2()}',
        reply_markup=ForceReply(selective=True),
    )







def getClickButtonData(update, context:CallbackContext):
    Supdate = update.callback_query
    chat_id = Supdate.message.chat.id
    user_id= Supdate.message.from_user.id
    all_admins = context.bot.get_chat_administrators(chat_id=chat_id)
    # print(context.bot.get_chat_administrators(chat_id=chat_id))
    CurrentMemberData = context.bot.get_chat_member(chat_id=chat_id,user_id = user_id).to_dict()
    logic = update.callback_query.data
    if chat_id in env.logged_user:
        #Changing Config
        if logic == 'CWM':
            env.method='CWM'
            Supdate.message.reply_text('Enter new welcome message')
            return
      



##################################
    # dispatcher.add_handler(CommandHandler("contact", contact))
    # dispatcher.add_handler(CommandHandler("site", site))
    # dispatcher.add_handler(CommandHandler("price", price))
    # dispatcher.add_handler(CommandHandler("airdrop", airdrop))
def contact(update:Update,context:CallbackContext)->None:
    update.message.reply_text('Youtube  : https://m.youtube.com/channel/UCiSOxpIRlIf5O2mm4YlmUVw\n\nPage Twitter : https://twitter.com/PogoSwap?t=NaRL5LvaVvgLodfSF5Ks-w&s=08 Twitter (https://twitter.com/PogoSwap?t=NaRL5LvaVvgLodfSF5Ks-w&s=08) PogoSwap (@PogoSwap) | Twitter The latest Tweets from PogoSwap (@PogoSwap). The World Class Decentralized Digital Asset Exchange | Trade Becomes Easy | Startup Incubator IDO #bitcoin',parse_mode='HTML')
    return
def price(update:Update,context:CallbackContext)->None:
    if not len(env.price)<=0:
        update.message.reply_text(env.price,parse_mode='HTML')
    return
def site(update:Update,context:CallbackContext)->None:
    update.message.reply_text('Site: https://www.pogoswap.io',parse_mode='HTML')
    return
def airdrop(update:Update,context:CallbackContext)->None:
    update.message.reply_text('Airdropbot : https://t.me/PogoSwapbot',parse_mode='HTML')
    return
def contract(update:Update,context:CallbackContext)->None:
    update.message.reply_text('START : 09/09\n🆓️Airdrop : POGOSWAP\n‼️TOKEN : POGO\n SMART CONTRACT :0x553B3De469EA8A9940C5549D170f541409b05DD4\n🏦 Distribution Date : 18 October, 2021 \n🔖 AirDrop registration link : \nhttps://t.me/PogoSwapbot\n TASK\n1️⃣ Join ourTelegram group \n2️⃣ Follow Twitter and retweet pinned\n3️⃣ follow our youtube Channel\n4️⃣ Register your BinanceSmartChain BSC',parse_mode='HTML')
    update.message.reply_text('\n(Bep_20)wallet address\n⚠️ Please note that all AirDrop tokens are free, please do not spend a single cent on AirDrop \n⚠️   YOU CAN ALSO BUY POGO ON POGOSWAP BEFORE OUR LAUNCH IN OCTOBER',parse_mode='HTML')
    return



###############################################

def echo(update: Update, context: CallbackContext) -> None:
    user_name = update.message.from_user.name
    user_id = update.message.from_user.id

    print(f'user_name{user_name},id{user_id}')
    if not user_name in env.user_name_trace:
        env.user_name_trace.append(user_name)
        env.user_trace[str(user_name)]=user_id
    print(update.message.chat.id)
    print(context.bot.getMe())
    echo  = str(update.message.text)
    chat_id = update.message.chat.id
    if not update.message.chat.type=='private' :
        if not is_admin(update,context):
            #this part will check the messages :
            if init.detect_link(echo):
                update.message.reply_text('Please dont post external links')
                time.sleep(1.5)
                context.bot.deleteMessage(chat_id=update.message.chat.id, message_id=update.message.message_id)            
                return
            return
    else:
        if env.method == 'login':
            password = echo
            if str(env.pasowrd) == password :
                env.method = str()
                env.logged_user.append(chat_id)
                dashboard(update,context)
                update.message.reply_text('successfully logged in')
                return
            
            else:
                update.message.reply_text('Wrong password .... Please try again')
                return


        elif env.method == 'CWM':
                env.welcome_message = echo
                update.message.reply_text('changed successfully')
                return
        return 











def main() -> None:
    updater = Updater(env.API_KEY)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ban", ban))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("invite", invite_link))
    dispatcher.add_handler(CommandHandler("login", login))
    dispatcher.add_handler(CommandHandler("dash", dashboard))
    dispatcher.add_handler(CommandHandler("contact", contact))
    dispatcher.add_handler(CommandHandler("site", site))
    dispatcher.add_handler(CommandHandler("price", price))
    dispatcher.add_handler(CommandHandler("contract", contract))
    dispatcher.add_handler(CommandHandler("airdrop", airdrop))




    dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
    dispatcher.add_handler(MessageHandler(Filters.status_update.left_chat_member, left_member))


    dispatcher.add_handler(CallbackQueryHandler(getClickButtonData))
    ########### file_handlings
    dispatcher.add_handler(MessageHandler(Filters.voice, files))
    dispatcher.add_handler(MessageHandler(Filters.photo, files))
    dispatcher.add_handler(MessageHandler(Filters.video, files))
    dispatcher.add_handler(MessageHandler(Filters.document, files))
    dispatcher.add_handler(MessageHandler(Filters.sticker, files))
    ############
    #Message Handlings
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    #############
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
