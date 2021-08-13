from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('m2xxVFQMnMPN0P+A9SGTEIVpGuA1ZirtFQNwn9FidRcZA1lpEYujtJVNgXn1dQPkxWmlbnI+FS/vbZ6q2cqlBYslg5HeknRdPIr87sS3P0TihyHJybHBu/sZ7/goTsNmJFS936fKy+oBukejJDFQlAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('46856d7cd9e253c966d0fb974fbdebaf')

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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = ['Never gonna give you up', 'never gonna let you down'
    ]

    if msg == ['hi', 'Hi']:
        r = 'yo'
    elif msg == 'hello':
        r = 'sup'
    elif msg ==


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()