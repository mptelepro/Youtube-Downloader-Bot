from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/mpazaanbot")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/mpazaan")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/help for More info.example `https://youtu.be/r-CDZm1JmY4` "
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
