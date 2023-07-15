'''
In this code we learn how to create a table, add, delete and update elements into the table in a database using postgres
To create a table, add, delete and update elements into the table we use SQL statements as shown below
'''

import nextcord
import asyncpg

bot = commands.Bot(command_prefix=">", intents=nextcord.Intents.all())

DB_HOST = 'localhost'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database_name'
TABLE_NAME = 'your_table_name'

db_pool = None

@bot.event
async def on_ready():
    global db_pool
    db_pool = await asyncpg.create_pool(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    
    async with db_pool.acquire() as cursor:
        await cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100),
                age INT
            )
        ''')
    print(f"Bot is ready. Connected to {DB_NAME} database.")

@bot.command()
async def insert(ctx, name: str, age: int):
    async with db_pool.acquire() as cursor:
        await cursor.execute(f"INSERT INTO {TABLE_NAME} (name, age) VALUES ($1, $2)", name, age)
    await ctx.send(f"Values inserted successfully.")

@bot.command()
async def update(ctx, id: int, age: int):
    async with db_pool.acquire() as cursor:
        await cursor.execute(f"UPDATE {TABLE_NAME} SET age = $1 WHERE id = $2", age, id)
    await ctx.send(f"Values updated successfully.")

@bot.command()
async def delete(ctx, id: int):
    async with db_pool.acquire() as cursor:
        await cursor.execute(f"DELETE FROM {TABLE_NAME} WHERE id = $1", id)
    await ctx.send(f"Values deleted successfully.")

bot.run("TOKEN")
