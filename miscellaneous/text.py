'''
In this code we generate the message by displaying each character individually by looping through the message
'''

@bot.command()
async def msg(ctx, *, message: str):
    main_message = ""
    
    msg = await ctx.send("Thinking...")
    for i in message:
        main_message += i
        
        await msg.edit(content=main_message)

bot.run("TOKEN")
