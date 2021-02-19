# my api id        2388554
# my api hash      3e30cf236573b82381da92246f9d9586

# -1001231834270, -1001087489823

from telethon import TelegramClient, events
import logging
import json
import re

#load in keywords
with open("text/keywords.json") as json_file:
    keyWords = [i.upper() for i in json.load(json_file)["keywords"]]
    print("\n Keywords: ", keyWords)

#load in blacklist
with open("text/blacklist.json") as json_file:
    black = [i.upper() for i in json.load(json_file)["black"]]
    print("\n Black listed words: ", black)

#load in currencies
with open("text/currencies.json") as json_file:
    currency = [i.upper() for i in json.load(json_file)["currency"]]
    print("\n Currencies: ", currency)

with open("text/caps.json") as json_file:
    caps = [i.upper() for i in json.load(json_file)["caps"]]
    caps = caps + currency
    print("\n Caps: ", caps)


#load in publishers
with open("text/receiveFrom.json") as json_file:
    skemmers = json.load(json_file)["skemmerMan"]
    print("\n WOlfs: ", skemmers)

#load in subscribers
with open("text/sendTo.json") as json_file:
    sheeps = json.load(json_file)["sheeple"]
    print("\n sheeps", sheeps)

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

print("\nBot Running...")
# Use your own values from my.telegram.org
api_id = 2388554
api_hash = "3e30cf236573b82381da92246f9d9586"
client = TelegramClient("anon", api_id, api_hash)

# listen to publishers


@client.on(events.NewMessage(from_users=skemmers))
async def my_event_handler(event):
    rawMsg = event.raw_text  # message receive
    newMsg = rawMsg  # creates another instance to store message to edit later on
    print(rawMsg)
    # checks if message contains keywords and currency [i for i in keyWords if re.search(i, rawMsg, re.IGNORECASE)] and
    if[o for o in currency if re.search(o, rawMsg, re.IGNORECASE)]:
        # checks if message does not contain blacklisted words
        if not [j for j in black if re.search(j, rawMsg, re.IGNORECASE)]:
            # Caps the currency pairs
            for k in caps:
                newMsg = re.sub(k, k.upper(), newMsg, flags=re.IGNORECASE)

        # Send message to suscribers
        print("Sending\n")
        for x in sheeps:
            await client.send_message(x, newMsg)

# Starts and run session until disconnected
client.start()
client.run_until_disconnected()
