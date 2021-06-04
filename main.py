import discord
import random
import re

pattern = r'(\d{1,2})?d(\d{1,2})?'
prefix = '```Rolled:'
suffix = '```'
separator = ','
linebreak = 10

client = discord.Client()


def table_gen(nums):
    tbl = ''
    for i in range(len(nums)):
        if i != 0:
            tbl += separator

        if i % linebreak == 0:
            tbl += '\n'

        if nums[i] // 10 == 0:
            tbl += '  '
        else:
            tbl += ' '

        tbl += str(nums[i])

    return tbl


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    matches = re.fullmatch(pattern, message.content)
    if matches is not None:
        numbers = []
        if matches.group(1):
            if matches.group(2):
                for i in range(int(matches.group(1))):
                    numbers.append(random.randint(1, int(matches.group(2))))

            else:
                for i in range(int(matches.group(1))):
                    numbers.append(random.randint(1, 6))

        else:
            numbers.append(random.randint(1, 6))

        await message.channel.send(prefix + table_gen(numbers) + suffix)

token = open('token', 'r').read()
client.run(token)
