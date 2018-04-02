from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('AzH87TcvfQKLWSRFu2ziKsU10gIyDwK5TeMlgmnzoF+M3WAW1Jdtvmjq/BlF4wqlYNicqEJ3QzmReL7EQ5/dbxlNNROsVLMNMAZ6yJquRVTTNEG2msiups++EZJmHrjj2cPYsIs2O2tpiCFykonofgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('d4ad2ad65af463cd625172cb419f50e0')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)

 

def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, message)
    text = event.message.text   
    #recipeWeb = 'https://icook.tw/recipes/search?q=' + text + '&ingredients='
    #r = requests.get(recipeWeb)  
    if text == 'Hi':
        line_bot_api.reply_message(event.reply_token, 
        TextSendMessage(text='Hi, mate'))  
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text))  
     
       
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
    

   
    
    
    
    
