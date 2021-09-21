def detect_link(text = str()):
    result = False
    link_sings=['.me','.com','.io','.health','.xyz','.net','.ru','.in','https://','http://','www.','.biz','.org','gmail','email','mail']
    for i in link_sings :
        if i in text:
            result = True
            break
    return result
    pass
# import requests
# requests.get('https://api.telegram.org/bot1920052812:AAH0amKfTNQ9PUS1zC9EC6wRVud0RAVyGS4/exportchatinvitelink?chat_id=-1001578624961')
