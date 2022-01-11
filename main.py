import discord
import os
import random
from keep_alive import keep_alive

client = discord.Client()

game = {'r':'Rock', 'p':'Paper', 's':'Scissors'}

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  elif message.content.startswith('-help'):
    await message.channel.send('Welcome to Rock, Paper, Scissor bot.\n Commands are as follows: \n1.-r = Chooses rock\n2.-p = Chooses paper\n3.-s = Chooses scissors\n All the best!!')
  
  elif message.content.startswith('-r'):
    ai = random.choice(['r','p','s'])
    await message.channel.send('You chose Rock')
    await message.channel.send('Computer chose {}'.format(game.get(ai)))
    await message.channel.send(winner(ai, message.content[1]))

  elif message.content.startswith('-p'):
    ai2 = random.choice(['r','p','s'])
    await message.channel.send('You chose Paper')
    await message.channel.send('Computer chose {}'.format(game.get(ai2)))
    await message.channel.send(winner(ai2, message.content[1]))

  elif message.content.startswith('-s'):
    ai3 = random.choice(['r','p','s'])
    await message.channel.send('You chose Scissors')
    await message.channel.send('Computer chose {}'.format(game.get(ai3)))
    await message.channel.send(winner(ai3, message.content[1]))
  
def winner(comp, human):
  if comp==human:
    return 'Tie'
  elif comp=='r':
    if human=='p':
        return 'You win'
    elif human=='s' :
        return 'You lose'
  elif comp=='p':
    if human=='r':
        return 'You lose'
    elif human=='s' :
        return 'You win'
  elif comp=='s':
    if human=='r':
        return 'You win'
    elif human=='p':
        return 'You lose'

keep_alive()

my_secret = os.environ['token']
client.run(my_secret)