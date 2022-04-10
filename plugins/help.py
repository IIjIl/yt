from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"**- أي استفسار أو خطأ أو مشكلة تواجهك راسل المطور :** @HssHH"
    await message.reply_text(helptxt)
