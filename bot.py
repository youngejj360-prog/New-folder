import os
import discord

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
                        print("Command triggered successfully!")
                        break
            except Exception as e:
                print(f"Error triggering command: {e}")

client = MyClient()
client.run(os.getenv("USER_TOKEN"), bot=False)