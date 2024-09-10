from discord.ext import commands, tasks
import discord
import pytz #pip install pytz
import datetime
from dataclasses import dataclass

BOT_TOKEN = "Insert Your Bot Token Here"
CHANNEL_ID = "Insert Your Channel ID Here"
MAX_SESSION_TIME_MINUTES = 30

@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
session = Session()

#Change to your local timezone
local_tz = pytz.timezone('America/Chicago')

#Converts a UTC datetime object to a local datetime object
def convert_to_local(utc_dt):
    return utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)

#When the bot is ready, print a message to the console
@bot.event
async def on_ready():
    print("Hello! Study bot is ready to go!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Study bot is ready to go!")

#Bot updates the user on how long they've been studying (MAX_SESSION_TIME_MINUTES)
@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=2)
async def break_reminder():

    #Ignore the first execution of this command
    if break_reminder.current_loop == 0:
        return

    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"**Time to take a break!** You've been studying for {MAX_SESSION_TIME_MINUTES} minutes.")

#Start the study session command
@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("Session is already active!")
        return

    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    local_time = convert_to_local(ctx.message.created_at)
    human_readable_time = local_time.strftime("%H:%M:%S %p")
    break_reminder.start()
    await ctx.send(f"New session started at {human_readable_time}!")

#End the study session command
@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return

    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(datetime.timedelta(seconds=duration))

    hours, remainder = divmod(int(duration), 3600)
    minutes, seconds = divmod(remainder, 60)
    human_readable_duration = f"{hours} hours, {minutes} minutes, {seconds} seconds"


    break_reminder.stop()   
    await ctx.send(f"Session ended after {human_readable_duration}!")

#Shutdown the bot command
@bot.command()
async def shutdown(ctx):
    await ctx.send("Goodbye! Shutting down now...")
    await bot.close()

bot.run(BOT_TOKEN)