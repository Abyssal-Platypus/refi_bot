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

**Note**
This code will not run in discord in its current state.
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

#class GetMerc():
#    def merc(s):
#        merc_name = s
#        merc_num = merc_list.Mercs.legendary(merc_name)
#        return merc_num

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
        
        if message.content.startswith('Wiggle Bot help'):
            await channel.send('Command "$hello" to greet Wiggle Bot.')
            await channel.send(
                'Command "$tell me a joke" to get a horrible dad joke.')

"""
This code is under construction for the BD Book connection, the response still 
section still needs to be worked out. 
"""
#        if message.content.startswith('$find legend'):
#            await channel.send('What merc do you want to find?')
#            def check(reaction, user):
#                return user == message.author
#            await channel.send(
#                f'book.browndust.app/detail.html?id={GetMerc.merc.merc_num()}'
#                )



client = MyClient()
client.run()