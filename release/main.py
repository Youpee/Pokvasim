from time import sleep
import requests
import json


class Pokvasim:
    def __init__(self):
        self.msgid_ignore = -1
        with open("config.json", encoding='utf-8') as cj:
            self.config = json.load(cj)
            self.api_token = self.config["API_TOKEN"]
            self.idanonkvas = self.config["CHANNEL_ID"]
            self.your_id = self.config["YOUR_ID"]

    def run(self):
        while (True):
            updates = self.update()
            if (not updates):
                break
            if (self.check_ignore_id(updates)):
                if ("message" in updates):
                    self.copy_message(self.idanonkvas,
                                      updates["message"]["chat"]["id"],
                                      updates["message"]["message_id"])
                    self.msgid_ignore = updates["message"]["message_id"]

                elif ("channel_post" in updates):
                    self.copy_message(self.your_id,
                                      self.idanonkvas,
                                      updates["channel_post"]["message_id"])
                    self.msgid_ignore = updates["channel_post"]["message_id"]

            sleep(0.1)

    def check_ignore_id(self, updates):
        text = "message" if "message" in updates else "channel_post"
        return updates[text]["message_id"] != self.msgid_ignore

    def update(self):
        try:
            return requests.get(f"https://api.telegram.org/bot{self.api_token}/getUpdates?offset=-1").json()["result"][0]
        except:
            print("напиши чёт боту в лс")
            return False

    def copy_message(self, chat_id: int, from_chat_id: int, id_msg: int):
        requests.get(
            f"https://api.telegram.org/bot{self.api_token}/copyMessage?chat_id={chat_id}&from_chat_id={from_chat_id}&message_id={id_msg}")


Pokvasim().run()
