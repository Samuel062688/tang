)

app = Flask(__name__)

line_bot_api = LineBotApi('hNpPhmboDyDWoE2pq4it9NulNEbpdnJZ3u+TQu+r+tGnntgL9yENMUPXJR7o3aPJfu3xPPkz7fOOnMQY/YO22YRkjAqPYXfiN8df19oe1kOcmmtlBiV5UaTFbPsw43MuKx3xvGsweZQbskQabNPw8gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('51ff2e343fd6714d93217a397dfc8a29')

# 推給你自己 
line_bot_api.push_message('Udd51a4dd41f3b69c4fd81a3034376256', TextSendMessage(text='(後臺訊息)啟動Sam探索共學ECHO機器人!'))

# 推給某個User
# line_bot_api.push_message('Udd51a4dd41f3b69c4fd81a3034376256', TextSendMessage(text='(後臺訊息)啟動探索共學ECHO機器人!'))

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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
