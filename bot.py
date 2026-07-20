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
            print("!startpacks triggered, checking channel...")
            channel = self.get_channel(CHANNEL_ID)
            if not channel:
                channel = await self.fetch_channel(CHANNEL_ID)
            
            try:
                commands = await channel.application_commands()
                for cmd in commands:
                    if cmd.name == "packs":
                        print("Found /packs command. Attempting to execute...")
                        
                        # Targets the specific 'multipackly' subcommand if it exists
                        target_cmd = next((c for c in cmd.children if c.name == "multipackly"), cmd)
                        
                        await target_cmd(channel=channel, packs=75, fast_open=True)
                        print("Command sent successfully!")
                        return
                        
                print("Could not find the /packs command in this channel.")
            except Exception as e:
                print(f"Error triggering command: {e}")

Thread(target=run_server).start()
client = MyClient()
client.run(os.getenv("USER_TOKEN"))