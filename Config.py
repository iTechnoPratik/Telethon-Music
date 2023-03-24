import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6176174815:AAGhrtfu-pga1XXKSKR2Cmykg0fwjvOKYx0")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOLgBuyd3cbxqGIk0HBHht7l3CHPuQeZ8pnysynSJGQNTpxIA1qUkySnK91eB-2Em3ozHJxcY_5yU_Ae36fSKDXkVU3BgU4gTHiMYVagST5dA5BKDc25Dl3_EOL6Zz-ZGp5kWw01o4KrCRz6i75I6G78uY-6b7iWLR1QTgD1N5IRdMle57YBXSq1AzIaJANmCT9ZkTkg3cgBEhixDNh-0HZEwIBppvwQjkhRP-4hfQysyCcZc4wJxWKZsuRJ2ProV0ZIpV4AkxYBCjUVCw4-NjaLTenTkfIZaWyMhCrebYS6I36IowXv2OVTkqe9sC92aGhuLxju1MEk5ALjEBUQwFHMY5IQ=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
