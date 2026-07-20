import asyncio
import os
import discord
from discord.ext import commands

CHANNEL_ID = 1517270182089719868

class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", self_bot=True, intents=discord.Intents.default())

    async def on_ready(self):
        print(f"Logged in as {self.user}")

    async def on_message(self, message):
        if message.author == self.user and message.content == "!startpacks":
            channel = message.channel
            commands_list = await channel.application_commands()
            for cmd in commands_list:
                if cmd.name == "packs":
                    await cmd(channel=channel, packs=75, fast_open=True)
                    break
        await self.process_commands(message)

client = MyClient()
client.run(os.getenv("USER_TOKEN"))