@bot.command()
async def GetChannelHistory(ctx,ID):
    ID = ''.join(x for x in ID if x not in "<#>")
    channel = bot.get_channel(int(ID))
    messages = await channel.history().flatten()
    with open("output.txt", "wb") as file:
        file.truncate(0)
        for message in messages:
            file.write(f'sent by {message.author.name}: \n『{message.content}』\n'.encode('UTF-8'))

    with open("output.txt", "rb") as file:
        await ctx.send(file=discord.File(file, "output.txt"))
