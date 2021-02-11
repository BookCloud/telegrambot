# my api id        2388554
# my api hash      3e30cf236573b82381da92246f9d9586

# -1001231834270, -1001087489823

from telethon import TelegramClient, events
import logging
import json

with open("text/keywords.json") as json_file:
    data = json.load(json_file)
    keyWord = data["keywords"]
    editedKeywords = []
    for i in range(len(keyWord)):
        new = keyWord[i].upper()
        editedKeywords.append(new)

    print(editedKeywords)

with open("text/blacklist.json") as json_file:
    data = json.load(json_file)
    black = data["black"]
    editedBlack = []
    for i in range(len(black)):
        new = black[i].upper()
        editedBlack.append(new)

    print(editedBlack)

with open("text/currencies.json") as json_file:
    data = json.load(json_file)
    currency = data["currency"]
    editedCurr = []
    for i in range(len(currency)):
        new = currency[i].lower()
        editedCurr.append(new)

    print(editedCurr)


with open("text/receiveFrom.json") as json_file:
    data = json.load(json_file)
    skemmers = data["skemmerMan"]
    print(skemmers)


with open("text/sendTo.json") as json_file:
    data = json.load(json_file)
    sheeps = data["sheeple"]
    print(sheeps)

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)
print("Bot Running...")
# Use your own values from my.telegram.org
api_id = 2388554
api_hash = "3e30cf236573b82381da92246f9d9586"


client = TelegramClient("anon", api_id, api_hash)


@client.on(events.NewMessage(from_users=skemmers))
async def my_event_handler(event):
    msg = event.raw_text
    txt = msg.upper()
    print(msg)
    if [ele for ele in editedKeywords if (ele in txt)]:
        if not [j for j in editedBlack if (j in txt)]:
            for i in editedCurr:
                msg = ' '.join(
                    [i.upper() if idx.lower() == i else idx for idx in msg.split()])

            print("send")
            for x in sheeps:
                await client.send_message(x, msg)


client.start()
client.run_until_disconnected()
