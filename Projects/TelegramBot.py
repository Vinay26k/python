import time
import json
import requests
import urllib

from DbHelperI import DbHelper
db = DbHelper()

#Default variables keep it in CAPS
TOKEN = r'YOUR TOKEN HERE'
URL = r'https://api.telegram.org/bot{0}/'.format(TOKEN)
#print(URL)

#Get things from url, vinay dont mess with variables keep it understandable

def get_url(url):
    response = requests.get(url)
    return response.content.decode('utf8')

#print(get_url(URL))

def get_json_from_url(url):
    content = json.loads(get_url(url))
    return content

def get_me():
    url = URL + 'getme'
    return get_json_from_url(url)

def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={0}".format(offset)
    return get_json_from_url(url)

#newly adding get_last_update_id, handle_updates, keyboard

def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {'keyboard': keyboard, 'one_time_keyboard': True}
    return json.dumps(reply_markup)

def hide_keyboard():
    keyboardHide = {'hide_keyboard' :True}
    return json.dumps(keyboardHide)

def get_last_update_id(updates):
    update_ids=[]
    for update in updates['result']:
        update_ids.append(int(update['update_id']))
    return max(update_ids)
    
def get_last_chat_id_and_text(updates):
    #updates is dictionary datastructure with ok and result as keys :)
    total_updates = len(updates['result'])
    last_update = total_updates - 1
    text = updates['result'][last_update]['message']['text']
    chat_id = updates['result'][last_update]['message']['chat']['id']
    return (text,chat_id)

def send_message(text, chat_id, reply_markup = None):
    text = urllib.parse.quote_plus(text)
    url= URL + "sendMessage?text={0}&chat_id={1}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += '&reply_markup={0}'.format(reply_markup)
    get_url(url)
    #print("DOne")
    
welcome = '''
Welcome to your personal To Do list.
Send any text to me and I'll store it as an item.
Extra commands Send
/start to show this again
/show to show tasks
/done to remove items
/exit to terminate any process
Bot by @vinay26k
'''

def not_empty(chat):
    if len(db.get_items(chat)):
        return True
    else:
        return False

def add(text,chat):
    db.add_item(text,chat)
    items = db.get_items(chat)
    message = "\n".join(items)
    send_message(message, chat)
    
def handle_updates(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        items = db.get_items(chat)
        if text == "/done":
            #print(len(db.get_items(chat)))
            if len(db.get_items(chat)):
                keyboard = build_keyboard(items)
                send_message("Select an item to delete", chat, keyboard)
            else:
                #print(len(db.get_items(chat)))
                keyboard = hide_keyboard()
                send_message("All tasks completed, add more tasks",chat,keyboard)
                #send_message("All tasks completed, add more tasks",chat,None)
                #items =['/exit']
                #keyboard = build_keyboard(items)
                #send_message("All tasks completed, add more tasks",chat,keyboard)
        elif text == "/start":
            send_message(welcome,chat)
        elif text == "/show":
            if not_empty(chat):
                items = db.get_items(chat)
                message = "\n".join(items)
                send_message(message, chat,None)
            else:
                send_message("All tasks completed, add more tasks",chat,None)
        elif text=='/exit':
            keyboard = hide_keyboard()
            send_message("Process terminated",chat,keyboard)
        elif text.startswith("/"):
            send_message('Process terminated',chat,None)
            continue
        
            continue
        elif text in items:
            db.delete_item(text,chat)
            items = db.get_items(chat)
            n = len(items)
            if n:
                keyboard = build_keyboard(items)
                send_message("Select an item to delete\n or /exit to terminate", chat, keyboard)
            else:
                #items =['/exit']
                #keyboard = build_keyboard(items)
                #send_message("All tasks completed, add more tasks",chat,keyboard)
                #print(len(db.get_items(chat)))
                keyboard = hide_keyboard()
                send_message("All tasks completed, add more tasks",chat,keyboard)
        else:
            add(text,chat)
            '''
            db.add_item(text,chat)
            items = db.get_items(chat)
            message = "\n".join(items)
            send_message(message, chat)'''


#modified main now 
def main():
    db.setup()
    last_update_id = None
    while True:
        #print("Getting Updates")
        updates = get_updates(last_update_id)
        if(len(updates['result']))>0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)

if __name__ == '__main__':
    main()


