from time import sleep
import requests
import json


class AnonEditMessage:
    def __init__(self):
        self.msgid_ignore = -1
        with open("config.json", encoding='utf-8') as cj:
            self.config = json.load(cj)
            self.api_token = self.config["API_TOKEN"]
            self.idanonkvas = self.config["CHANNEL_ID"]

    def run(self):
        while (True):
            updates = self.update()
            if (not updates):
                break

            if ("channel_post" in updates and self.check_ignore_id(updates)):
                if ("/e" in updates["channel_post"]["text"] and "reply_to_message" in updates["channel_post"]):
                    textList = updates["channel_post"]["text"].split()
                    if (len(textList) > 1):
                        self.editMessageText(
                            self.idanonkvas,
                            updates["channel_post"]["reply_to_message"]["message_id"],
                            " ".join(textList[1:]))
                        self.deleteMessage(
                            self.idanonkvas, updates["channel_post"]["message_id"])

                        self.msgid_ignore = updates["channel_post"]["message_id"]
                    else:
                        self.deleteMessage(
                            self.idanonkvas, updates["channel_post"]["message_id"])

            sleep(0.3)

    def check_ignore_id(self, updates):
        typeMsg = "message" if "message" in updates else "channel_post"
        return updates[typeMsg]["message_id"] != self.msgid_ignore

    def update(self):
        try:
            return requests.get(f"https://api.telegram.org/bot{self.api_token}/getUpdates?offset=-1").json()["result"][0]
        except:
            print("напиши чёт боту в лс")
            return False

    def deleteMessage(self, chat_id: int, msg_id: int):
        return requests.get(
            f"https://api.telegram.org/bot{self.api_token}/deleteMessage?chat_id={chat_id}&message_id={msg_id}").json()

    def editMessageText(self, chat_id: int, msg_id: int, text: str):
        return requests.get(f"https://api.telegram.org/bot{self.api_token}/editMessageText?chat_id={chat_id}&message_id={msg_id}&text={text}")


AnonEditMessage().run()
