import re
from random import choice, randint

from chitanda import BotError
from chitanda.util import register


@register('choose')
async def call(*, bot, listener, target, author, message, private):
    """Chooses one of many provided options."""
    match = re.match(r'(\d+) *- *(\d+)', message)
    if match:
        return randint(int(match[1]), int(match[2]))
    elif ',' in message:
        return choice([c.strip() for c in message.split(',')])
    elif ' ' in message:
        return choice([c.strip() for c in message.split(' ')])
    raise BotError('No options found.')
