import asyncio
import logging
import config
from pyromod import listen
from pyrogram import Client, idle, __version__
from pyrogram.raw.all import layer
import collections
import collections.abc
import sys
import types

import collections
import collections.abc
import sys
import types

# 1. Collections compatibility patch
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableMapping = collections.abc.MutableMapping
collections.Sequence = collections.abc.Sequence
collections.MutableSet = collections.abc.MutableSet  # <--- Add this line!

# 2. Ravenclaw/Chronometry Patch
try:
    import ravenclaw.preprocessing
except ImportError:
    m = types.ModuleType("ravenclaw.preprocessing")
    sys.modules["ravenclaw.preprocessing"] = m
    ravenclaw.preprocessing = m

if not hasattr(ravenclaw.preprocessing, 'Polynomial'):
    ravenclaw.preprocessing.Polynomial = type('Polynomial', (), {})
if not hasattr(ravenclaw.preprocessing, 'Normalizer'):
    ravenclaw.preprocessing.Normalizer = type('Normalizer', (), {})

# ... existing code (imports like from pyromod import listen, etc)

logging.basicConfig(level=logging.INFO)
plugins = dict(root="plugins")
bot = Client('ssh', api_id=config.app_id, api_hash=config.app_hash, bot_token=config.token, plugins=plugins)


async def main():
    await bot.start()
    me = await bot.get_me()
    print(f"\n{me.first_name} with Pyrogram v{__version__} (Layer {layer}) started on {me.username}.")
    await idle()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
