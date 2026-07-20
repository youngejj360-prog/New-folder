import os
import discord
import asyncio
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_running = False

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author.id != self.user.id:
            return

        if message.content == "!startpacks":
            if self.is_running:
                print("Script is already running.")
                return
            
            self.is_running = True
            print("Loop started.")
            channel = self.get_channel(CHANNEL_ID) or await self.fetch_channel(CHANNEL_ID)
            
            while self.is_running:
                try:
                    commands = await channel.application_commands()
                    for cmd in commands:
                        if cmd.name == "packs":
                            target_cmd = next((c for c in cmd.children if c.name == "multipackly"), cmd)
                            await target_cmd(channel=channel, packs=75, fast_open=True)
                            print("Command sent. Waiting 16 seconds...")
                            break
                except Exception as e:
                    print(f"Error: {e}")
                
                # Wait 16 seconds before the next loop
                if self.is_running:
                    await asyncio.sleep(16)

        elif message.content == "!stoppacks":
            self.is_running = False
            print("Loop stopped.")

Thread(target=run_server).start()
client = MyClient()
client.run(os.getenv("USER_TOKEN"))