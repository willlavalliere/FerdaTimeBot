import discord
from ferda_time_translator.translator import *
import os


class FerdaTimeBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        msg = message.content.lower()
        if "what are all the times" in msg:
            await message.channel.send(get_all_ferda_times())
        if "time" in msg or "when" in msg:
            await message.channel.send(get_current_ferda_time())
        if "suck" in msg and "me" in msg:
            await message.channel.send(':eggplant: :pleading_face:')
            await message.channel.send(f'@<{message.author.id}>')
        if not msg.startswith('!ferdatime') and not msg.startswith('!ft'):
            return
        if len(msg.split()) == 1:
            await message.channel.send(get_current_ferda_time())
        else:
            try:
                dt = datetime.strptime(msg.split()[1], "%H:%M")
                await message.channel.send(get_ferda_time(dt))
            except Exception as e:
                await message.channel.send('Invalid time format. Please use 24-hour format.\n'
                                           'Example: 15:30', delete_after=10)


intents = discord.Intents.default()
intents.message_content = True

client = FerdaTimeBot(intents=intents)

client.run(os.environ['DISCORD_BOT_TOKEN'])
