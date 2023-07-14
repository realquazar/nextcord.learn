import asyncio
import aiohttp
import nextcord

async def send_webhook(url, content):
    async with aiohttp.ClientSession() as session:
        webhook = nextcord.Webhook.from_url(url, session=session)
        await webhook.send(content)

  asyncio.send(send_webhook("https://url_link", "Content"))
