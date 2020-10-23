#!/usr

    
from tobrot.get_cfg import get_config


class Commandi:
    LEECH = get_config(
        "COMMANDI_LEECH",
        "leech@speedlestbot"
    )
    PURGE = get_config(
        "COMMANDI_PURGE",
        "purge@speedlestbot"
    )
    YTDL = get_config(
        "COMMANDI_YTDL",
        "ytdl@speedlestbot"
    )
    STATUS = get_config(
        "COMMANDI_STATUS",
        "status@speedlestbot"
    )
    CANCEL = get_config(
        "COMMANDI_CANCEL",
        "cancel@speedlestbot"
    )
    EXEC = get_config(
        "COMMANDI_EXEC",
        "exec@speedlestbot"
    )
    EVAL = get_config(
        "COMMANDI_EVAL",
        "eval@speedlestbot"
    )
    RENAME = get_config(
        "COMMANDI_RENAME",
        "rename@speedlestbot"
    )
    UPLOAD = get_config(
        "COMMANDI_UPLOAD",
        "upload@speedlestbot"
    )
    HELP = get_config(
        "COMMANDI_HELP",
        "help"
    )
    SAVETHUMBNAIL = get_config(
        "COMMANDI_SAVETHUMBNAIL",
        "savethumbnail@speedlestbot"
    )
    CLEARTHUMBNAIL = get_config(
        "COMMANDI_CLEARTHUMBNAIL",
        "clearthumbnail@speedlestbot"
    )
    GET_RCLONE_CONF_URI = get_config(
        "COMMANDI_GET_RCLONE_CONF_URI",
        "getrcloneconfuri"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMANDI_UPLOAD_LOG_FILE",
        "log"
    )
    GET_RCLONE_CONF_URI = get_config(
        "COMMANDI_GET_RCLONE_CONF_URI",
        "getrcloneconfuri"
    )
    UPLOAD_LOG_FILE = get_config(
        "COMMANDI_UPLOAD_LOG_FILE",
        "log"
    )
