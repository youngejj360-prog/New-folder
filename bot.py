import asyncio
import os
import discord

CHANNEL_ID = 1517270182089719868

class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user and message.content == "!startpacks":
            channel = message.channel
            commands = await channel.application_commands()
            for cmd in commands:
                if cmd.name == "packs":
                    await cmd.invoke(channel, packs=75, fast_open=True)
                    break

client = MyClient()
client.run(os.getenv("USER_TOKEN"), bot=False)