from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ]
    ]
    dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="IIᴘᴀᴜsᴇ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="▢sᴛᴏᴘ▢", callback_data=f"ADMIN Stop|{chat_id}"),
            InlineKeyboardButton(text="sᴋɪᴘ‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),

        ],
        [
            InlineKeyboardButton(text="▷ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="ʀᴇᴘʟᴀʏ↺", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴍᴏʀᴇ ๏", url="https://t.me/II_PBX1_II",
                
            ),
        ],
    ]
    return buttons


def queuemarkup(_, vidid, chat_id):

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],


        [
            InlineKeyboardButton(
                text="II ",
                callback_data=f"ADMIN Pause|{chat_id}",
            ),

            InlineKeyboardButton(
                text="▢ ", callback_data=f"ADMIN Stop|{chat_id}"
            ),

            InlineKeyboardButton(
                text="‣‣ ", callback_data=f"ADMIN Skip|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(text="▷ ", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="↺ ", callback_data=f"ADMIN Replay|{chat_id}"),
        ],
        [
            InlineKeyboardButton(text="𐏓 ⃪⃝🇺🇸 ꯭𝗗ᴇᴠɪ𝗟 ꯭༎ࠫ⛧‌", url="https://t.me/ll_mxni_ll"),
            InlineKeyboardButton(text="⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂⎯꯭ ꯭̽🌸", url="https://t.me/ll_BAD_BBY_ll"),
        ],
        [
            InlineKeyboardButton(
                text="๏ ᴍᴏʀᴇ ๏", url="https://t.me/II_PBX1_II",
                
            ),
        ],
    ]

    return buttons
