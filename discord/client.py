from asyncio import get_event_loop, sleep
from .gateway import DiscordGateway
from ..errors import ApiError
import asyncio

class Client:
    def __init__(self, loop:asyncio.AbstractEventLoop = None, version:int = 9, intents:int = 513, log:bool = True):
        self.log = log
        self.intents = intents
        self.baseurl = f"https://discord.com/api/v{version}"
        self.loop = asyncio.get_event_loop() if loop is None else loop
        self.ws = None
