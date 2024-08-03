import interactions
import requests
import os
import json

# Required configuration
bottoken = ""  # Your Discord bot token
appkey = "" # Your application key goes here
acckey = "" # Your account key goes here
appid = "" # Your application ID goes here
apptoken = "" # Your application token goes here

bot = interactions.Client(token=bottoken)

@bot.command(
  name="userid",
  description="Displays the user ID",
)
async def userid(ctx: interactions.CommandContext):
  await ctx.send(f"User ID: `{ctx.author.id}`")

@bot.command(
  name="serverid",
  description="Displays the server ID",
)
async def serverid(ctx: interactions.CommandContext):
  await ctx.send(f"Server ID: `{ctx.guild.id}`")

@bot.command(
  name="getvar",
  description="Getting value of a server-sided variable",
  options=[
    interactions.Option(
      name="varid",
      description="Your Variable ID",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def getvar(ctx: interactions.CommandContext, varid: str):
  var = varid
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)

  response = requests.get("https://eauth.us.to/api/command.php?sort=variable&varid=" +
                          var + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid + "",
                          headers=headers)
  await ctx.send(response.text)


@bot.command(
  name="genkey",
  description="Generate a new key",
  options=[
    interactions.Option(
      name="length",
      description="Length of the key (9 ~ 16)",
      type=interactions.OptionType.STRING,
      required=True,
    ),
    interactions.Option(
      name="rank",
      description="Rank given to the key",
      type=interactions.OptionType.STRING,
      required=True,
    ),
    interactions.Option(
      name="expire",
      description="Expire duration of the key",
      type=interactions.OptionType.STRING,
      required=True,
    ),
    interactions.Option(
      name="prefix",
      description="Prefix of the key",
      type=interactions.OptionType.STRING,
      required=False,  # Set required to False to make it optional
    ),
  ],
)
async def genkey(ctx: interactions.CommandContext, rank: str, expire: str,
                 length: str, prefix: str = ""):  # Set prefix to an empty string as default value
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=genkey&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&rank=" + rank + "&expire=" + expire + "&length=" +
                          length + "&prefix=" + prefix + "",
                          headers=headers)
  await ctx.send(response.text)

@bot.command(
  name="delkey",
  description="Delete a key",
  options=[
    interactions.Option(
      name="key",
      description="The key you wish to delete",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def delkey(ctx: interactions.CommandContext, key: str):
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=delkey&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&keyid=" + key + "",
                          headers=headers)
  await ctx.send(f"{response.text}")


@bot.command(
  name="delvar",
  description="Delete a variable",
  options=[
    interactions.Option(
      name="varname",
      description="The variable you wish to delete",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def delvar(ctx: interactions.CommandContext, varname: str):
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=delvar&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&varname=" + varname + "",
                          headers=headers)
  await ctx.send(f"{response.text}")


@bot.command(
  name="addvar",
  description="Add a variable",
  options=[
    interactions.Option(
      name="varname",
      description="A name your want",
      type=interactions.OptionType.STRING,
      required=True,
    ),
    interactions.Option(
      name="varvalue",
      description="A value your want",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def addvar(ctx: interactions.CommandContext, varname: str,
                 varvalue: str):
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=addvar&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&varname=" + varname + "&varvalue=" + varvalue + "",
                          headers=headers)
  await ctx.send(f"{response.text}")


@bot.command(
  name="adduser",
  description="Add a new user account",
  options=[
    interactions.Option(
      name="username",
      description="A name given to the user",
      type=interactions.OptionType.STRING,
      required=True,
    ),
    interactions.Option(
      name="password",
      description="Password for the user account",
      type=interactions.OptionType.STRING,
      required=True,
    ),
    interactions.Option(
      name="rank",
      description="Rank given to the user",
      type=interactions.OptionType.STRING,
      required=True,
    ),
    interactions.Option(
      name="expire",
      description="Expire duration of the user account",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def adduser(ctx: interactions.CommandContext, username: str,
                  password: str, rank: str, expire: str):
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=adduser&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&username=" + username + "&password=" + password +
                          "&rank=" + rank + "&expire=" + expire + "",
                          headers=headers)
  parts = response.text.split('|')
  message = '\n'.join(parts)
  await ctx.send(message)


@bot.command(
  name="deluser",
  description="Delete a user",
  options=[
    interactions.Option(
      name="username",
      description="The user you wish to delete",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def deluser(ctx: interactions.CommandContext, username: str):
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=deluser&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&username=" + username + "",
                          headers=headers)
  await ctx.send(f"{response.text}")


@bot.command(
  name="keydata",
  description="Obtain the properties of a key based on its ID",
  options=[
    interactions.Option(
      name="keyid",
      description="Your Key ID",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def keydata(ctx: interactions.CommandContext, keyid: str):
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=keydata&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&keyid=" + keyid + "",
                          headers=headers)
  parts = response.text.split('|')
  message = '\n'.join(parts)
  await ctx.send(message)


@bot.command(
  name="userdata",
  description="Obtain the properties of a user based on its name",
  options=[
    interactions.Option(
      name="username",
      description="Name of the account",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def userdata(ctx: interactions.CommandContext, username: str):
  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)
  
  response = requests.get("https://eauth.us.to/api/command.php?sort=userdata&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&username=" + username + "",
                          headers=headers)
  parts = response.text.split('|')
  message = '\n'.join(parts)
  await ctx.send(message)


@bot.command(
  name="resethwid",
  description="Reassigning the hardware ID for a user account to default",
  options=[
    interactions.Option(
      name="username",
      description="The user you wish to reset",
      type=interactions.OptionType.STRING,
      required=True,
    ),
  ],
)
async def resethwid(ctx: interactions.CommandContext, username: str):

  headers = {"User-Agent": "eauth"}
  userid = str(ctx.author.id)
  serverid = str(ctx.guild.id)

  
  response = requests.get("https://eauth.us.to/api/command.php?sort=hwidreset&appid=" +
                          appid + "&appkey=" + appkey + "&acckey=" + acckey + "&apptoken=" + apptoken + "&appid=" + appid + "&userid=" + userid + "&serverid=" + serverid +
                          "&username=" + username + "",
                          headers=headers)
  await ctx.send(response.text)

bot.start() # Launch the bot
