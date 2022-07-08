#  This is SMS sending
from calendar import c
from gettext import install
from vonage import Client, Sms

class initlib:
    def api_send(Num):
        client = Client(key="3be...", secret="8I2K...")
        sms = Sms(client)
            
        firstNum = Num[0]
        if '1' != firstNum:
            Num = '1' + Num
            print(Num)
        responseData = sms.send_message(
            {
                "from": "18335789034",
                "to": Num,
                "text": "A text message sent using the Nexmo SMS API",
            }
        )

        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully")
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
if __name__ == '__main__':
    initlib()