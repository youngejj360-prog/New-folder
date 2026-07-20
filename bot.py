import os
import discord
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running"

def run_server():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

CHANNEL_ID = 1517270182089719868

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.id == self.user.id and message.content == "!startpacks":
            channel = self.get_channel(CHANNEL_ID) or message.channel
            try:
                commands = await channel.application_commands()
                for cmd in commands:
                    if cmd.name == "packs":
                        await cmd.invoke(channel, packs=75, fast_open=True)
                        break
            except Exception:
                pass

Thread(target=run_server).start()
client = MyClient()
client.run(os.getenv("USER_TOKEN"))