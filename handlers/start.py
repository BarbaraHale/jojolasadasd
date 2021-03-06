from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="**Hello ππ» {}!**\n\nI **Can Play Music In Voice Chats of Telegram Groups.**I Have A **lot of cool feature that will amaze You!**\n\n**Click /cmdlist For More Help On My Usage β€**".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("β Add To Your Group β", url="https://t.me/RYTHMXBOT?startgroup=true")
            ],[
            InlineKeyboardButton("π¬ Group", url="https://t.me/rythmXsupport"),
            InlineKeyboardButton("Channel π", url="https://t.me/rythmXupdate")
            ],[
            InlineKeyboardButton("Commands π ", url="https://telegra.ph/Music-Bot-05-07")
            ]]
        ),
        disable_web_page_preview=True
    )
        
@Client.on_message(filters.command(["start", "start@RYTHMXBOT"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        text="**Music Bot Is Online β**",
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton(text="ποΈ Support Group ποΈ", url="https://t.me/rythmXsupport")
            ]]
        )
    )


@Client.on_message(filters.command(["cmdlist", "start@RYTHMXBOT"]) & filters.private & ~filters.channel)
async def cmdlist(_, message: Message):
    await message.reply_text(
        text="""**RΚΈΝ’Ν’THMπ Group Music Bot : Help Menu**

__Γ First Add Me To Your Group..
Γ Promote Me As Admin In Your Group With All Permission..__

**π· Common Commands.**

β’ `/play` - Song Name : __Plays Via Youtube__
β’ `/dplay` - Song Name : __Play Via Deezer__
β’ `/splay` - Song Name : __Play Via Jio Saavn__
β’ `/playlist` - __Show now playing list__
β’ `/current` - __Show now playing__

β’ `/song` - Song Name : __Get The Song From YouTube__
β’ `/vid` - Video Name : __Get The Video From YouTube__
β’ `/deezer` - song name : __download songs you want quickly via deezer__
β’ `/saavn` - song name : __download songs you want quickly via saavn__
β’ `/search` - YouTube Title : __(Get YouTube Search Query)__

**π· Group Admin Commands.**

β’ `/skip` : __Skips Music__
β’ `/pause` : __Pause Playing Music__
β’ `/resume` : __Resume Playing Music__
β’ `/end` : __Stops playing Music__
β’ `/reload` : __Reloads Admin List__
β’ `/userbotjoin` : __Assistant Joins The Group__
β’ `/userbotleave` : __Assistant Leaves From The Group.__""",
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="ποΈ Support Group ποΈ", url="https://t.me/rythmXsupport")
              ]]
          )
      )
