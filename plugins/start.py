from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("- Hasoni Alnajar", url="https://t.me/HssHH")],
    ])
    welcomed = f"**اهلا بك عزيزي في بوت التحميل من اليوتيوب<b>{message.from_user.first_name}</b>\n\n ارسل رابط المقطع لتنزيله**"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
