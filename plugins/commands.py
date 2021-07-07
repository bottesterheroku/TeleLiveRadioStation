"""
VC Radio Player, Telegram Voice Chat Userbot

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Hi, [{}](tg://user?id={})!\n\nI am Voice Chat Radio Player in\nChannels and Groups 24×7 NonStop.\n\nI can even Stream YouTube Live in VoiceChat!\n\nDeploy Your Own bot from [👉 here]Repo is under maintenance.\n\n▷Please Subscribe ❤️ @PatheticProgrammers</b>"
HELP = """**Only Admins Commands**:

**▷/radio:** Start Radio.
**▷/stop:** Stops Radio/LiveStream.
**▷/join:**  Join voice chat.
**▷/leave:**  Leave current voice chat
**▷/vc:**  Check which VC is joined.
**▷/mute:** Mute in Voice Chat.
**▷/unmute:** Unmute in Voice Chat.
**▷/pause:** Pause the Streaming.
**▷/resume:** Resume the paused Stream.
**▷/clean:** Clean RAW File's.
**▷/restart:** Restarts the Bot.
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('📻 Listen here Radio', url='https://t.me/PatheticProgrammers?voicechat'),
    ],
    [
        InlineKeyboardButton('👥 Group', url='https://t.me/PatheticProgrammers'),
        InlineKeyboardButton('Channel 📢', url='https://t.me/PatheticProgrammersChannel'),
    ],
    [
        InlineKeyboardButton('🆘 Helpful Commands 🆘', callback_data='help'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('📻 Listen here Radio', url='https://t.me/PatheticProgrammers?voicechat'),
        ],
        [
            InlineKeyboardButton('👥 Group', url='https://t.me/PatheticProgrammers'),
            InlineKeyboardButton('Channel 📢', url='https://t.me/PatheticProgrammersChannel'),
        ],
        [
            InlineKeyboardButton('🔰 How to Deploy 🔰', url='https://t.me/PatheticProgrammers),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
