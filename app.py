from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
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
    r = 'say that again? '

    if 'fuck' in msg:
        sticker_message = StickerSendMessage(
            package_id='6136',
            sticker_id='10551377'
        )

        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg in ['hi', 'Hi']:
        r = 'yo'
    elif msg in ['hello', 'Hello']:
        r = 'sup'
    elif msg in ['who are you', 'Who are you']:
        r = 'im your father'
    elif msg in ['never gonna let you down', 'Never gonna let you down']:
        r = 'Never gonna run around and desert you'
    elif 'sing' in msg:
        r = 'Never gonna give you up'
    
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()