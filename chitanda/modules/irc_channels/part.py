import asyncio

from chitanda import BotError
from chitanda.listeners import IRCListener
from chitanda.util import admin_only, allowed_listeners, args, register


@register('part')
@allowed_listeners(IRCListener)
@admin_only
@args(r'$', r'([#&][^\x07\x2C\s]{,199})$')
async def call(*, bot, listener, target, author, args, private):
    """Part a channel."""
    if args:
        channel = args[0]
        asyncio.ensure_future(listener.part(channel))
        return f'Attempted to part {channel}.'
    elif target != author:
        channel = target
        asyncio.ensure_future(listener.part(channel))
    else:
        raise BotError('This command must be ran in a channel.')
