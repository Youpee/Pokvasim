from time import sleep
import requests
import json


class CheckerSM:
    def __init__(self):
        with open("config.json", encoding='utf-8') as cj:
            self.config = json.load(cj)
            self.api_token = self.config["API_TOKEN"]
            self.idanonkvas = self.config["CHANNEL_ID"]
            self.editMsg = self.config["EDITMSG"]

    def run(self):
        while (True):
            updates = self.update()
            if (not updates):
                break

            msg_result = self.sendMessage(self.idanonkvas, f"?")["result"]

            self.deleteMessage(self.idanonkvas, msg_result["message_id"])

            if ("channel_post" in updates):
                self.editMessageText(
                    self.idanonkvas, self.editMsg, "author_signature" in msg_result)

            sleep(5)

    def check_ignore_id(self, updates):
        text = "message" if "message" in updates else "channel_post"
        return updates[text]["message_id"] != self.msgid_ignore

    def update(self):
        try:
            return requests.get(f"https://api.telegram.org/bot{self.api_token}/getUpdates?offset=-1").json()["result"][0]
        except:
            print("напиши чёт боту в лс")
            return False

    def sendMessage(self, chat_id: int, text: str):
        return requests.get(
            f"https://api.telegram.org/bot{self.api_token}/sendMessage?chat_id={chat_id}&text={text}").json()

    def deleteMessage(self, chat_id: int, msg_id: int):
        return requests.get(
            f"https://api.telegram.org/bot{self.api_token}/deleteMessage?chat_id={chat_id}&message_id={msg_id}").json()

    def editMessageText(self, chat_id: int, msg_id: int, typeMsg: bool):
        text = u"\U0001F7E5" if typeMsg else u"\U0001F7E9"
        return requests.get(f"https://api.telegram.org/bot{self.api_token}/editMessageText?chat_id={chat_id}&message_id={msg_id}&text={text * 15}")


CheckerSM().run()

