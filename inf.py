from telegram import InlineKeyboardButton   ,InlineKeyboardMarkup


class env:
    user_trace = dict()#{'name':id}
    user_name_trace = list()
    API_KEY = '1944399347:AAE06vUv8fUHl_tn0ie8yeIbsp5eMKhO_8A'

    welcome_message = "Welcome to the group \.  \n💥The project is a DEX  IDO\. A DEX is a decentralized cryptocurrency exchange to allow trusted third party and frictionless trading\. The initial IDO DEX offering is a place for new blockchain startups\. We are currently launching the POGO token which will give the possibility to those who have it to be able to participate in the launch of new future projects such as purrporn\.com and ticketgo\.io which will launch this fall on PogoSwap IDO☄️ "
    price = f'value:1.29$ \nThe POGO token is ready for purchase now at: pogoswap.io/ido/0 🥳🥳 ONLY ON DESKTOP COMPUTER 🤓 Connect to MetaMask on the Binance Smart Chain to buy your POGO token '
    file_text = f'Please <b>dont post</b> files or stickers only admin are allowed to do so'
    lef_message = f'Chat memeber left'
    pasowrd = str('testing321')
    logged_user = list()
    method = 'login'
    









    dash_keys =InlineKeyboardMarkup(   
    [
        [
            InlineKeyboardButton('change wlcome message' ,callback_data='CWM')
            ,InlineKeyboardButton('link Settings' ,callback_data='reverseLinkSettings')
        ]
        ,[
            InlineKeyboardButton('Language Settings' ,callback_data='language')
        ]
    ]
    )
