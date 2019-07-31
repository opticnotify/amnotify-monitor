import requests, json, time, discord
from discord_webhook import DiscordWebhook, DiscordEmbed

false = False
true = True

availablility = True 

def initialize():

    r = requests.get("https://amnotify.com/api/stock/available")

    data = json. loads(r.text)

    stockold = data["available"]

    return stockold

def monitor(stockold):

    r = requests.get("https://amnotify.com/api/stock/available")

    data = json.loads(r.text)

    if data["available"] != stockold and str(data["available"]).lower() == "true":
        webhook = DiscordWebhook(url = "https://discordapp.com/api/webhooks/605237481843195914/VEoGvhXdb_X6ypyg7E4d35SVJ01JkhhXllQ_z8oS2FakmMipp4167afI94snu5InL6UC")
        embed = DiscordEmbed(title = "AMNOTIFY STOCK MONITOR", description = "AMNOTIFY IS NOW IN STOCK!", color = 0x07fc03)
        embed.add_embed_field(name = "URL", value = "[Purchase Here](https://amnotify.com/purchase)")
        embed.set_footer(text = F"Optic Notify | AMNOTIFY STOCK MONITOR | {time.strftime('%H:%M:%S')}")
        webhook.add_embed(embed)
        webhook.execute()
    while str(data["available"]).lower() == "true":
        pass

print(' _______  __   __  __    _  _______  _______  ___   _______  __   __   ')
print('|   _   ||  |_|  ||  |  | ||       ||       ||   | |       ||  | |  |  ')
print('|  |_|  ||       ||   |_| ||   _   ||_     _||   | |    ___||  |_|  |  ')
print('|       ||       ||       ||  | |  |  |   |  |   | |   |___ |       |  ')
print('|       ||       ||  _    ||  |_|  |  |   |  |   | |    ___||_     _|  ')
print('|   _   || ||_|| || | |   ||       |  |   |  |   | |   |      |   |    ')
print('|__| |__||_|   |_||_|  |__||_______|  |___|  |___| |___|      |___|    ')


stockold = initialize()
print(f"{time.strftime('%H:%M:%S')} | MONITOR INITIALIZED")
print(f"{time.strftime('%H:%M:%S')} | MONITORING INITIALIZED")
while True: 
    monitor(stockold)

    