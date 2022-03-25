# discord-api-http

## What is this?

This is discord api low wrapper.

## sample

```python
import asyncio
from discord_api_http import HttpClient

async def main():
    async with HttpClient(token="Your_token") as session:
        print(await session.get("/users/@me"))

asyncio.run(main())
```
