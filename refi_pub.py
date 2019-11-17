#! /usr/bin/env python3
# coding=utf-8
"""
Hey guys, this is the bot here. Ill run over how each thing works.

The first block just below this is your imports, for running on 
Discord the discord module is very important. Its a module that
allows the code to interact with Discord effectively and saves a
ton of hours of work. 
json allows for file I/O as well as string
manipulation in this format. 
requests translates html to python for easier interaction between
the two codes.
merc_list is going to be the file that contains all of the mercs
for the GetMerc testing code. Phactos and I had discussed a bot that
will at least get you the page off of book.browndust.app that contains
the merc info.
"""
import discord
import json
import requests
import merc_list

class DadJoke():
    "This is just a little tool I built for generating a random dad joke. "
    def get_joke(id = None):
        endpoint = "http://icanhazdadjoke.com"
        url = endpoint + f'/j/{id}' if id else endpoint
        response = requests.get(url, headers = {"accept" : "application/json"})
        return json.loads(response.text)['joke']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as {0}!' .format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}' .format(message))
        channel = message.channel
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await channel.send('Hello @{.author}!' .format(message))

        if message.content.startswith('$tell me a joke'):
            await channel.send(f'{DadJoke.get_joke()}')
        
        if message.content.startswith('Refi help'):
            await channel.send('Command "$hello" to greet Refi Bot.')
            await channel.send('Command "$find <mercenary name>" to get a direct link to mercenary page.')
            await channel.send(
                'Command "$tell me a joke" to get a horrible dad joke.')

        if message.content.startswith('Refi are you there?'):
            await channel.send('Yes! Refi is here!')

        if message.content.startswith('$find '):
            sep = " "
            merc_name = message.content.split(sep, 1)[1]
            merc_number = merc_list.Mercs.merc_num(merc_name)
            refi = "refithea"
            if merc_name == str.lower(refi):
                await channel.send("Here I am!!")
            else:
                await channel.send(f"Here is {merc_name}!")
            await channel.send(f"https://book.browndust.app/detail.html?id={merc_number}")



client = MyClient()
client.run()