import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("20931654", ""))
API_HASH = getenv("13fcf3fbf97dfdfa4b55810a51706d5e", "")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6469443535:AAGo05fRyGab0-BwBXawd8RmdFKv2WOlMiw", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://myMusicBot:myMusicBot1234@atlascluster.yq7734n.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 180))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002009307077", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("551603105", "6203163206"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("micredomuisicbot")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-2c474dfe-446d-4dc6-8f1c-84e1afef360b")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/Learningbots79/LB_Music",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/BDGWINGAME3")
SUPPORT_CHAT = getenv("SUPPORT_GROUP", "https://t.me/FRIENDSHIP_CHAT_GROUP0")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("BQE_ZEYATWvqBtDyZRCUufkqmx_J7gXR6xL7p3p2pICljpNbMLKMI0hEL594tTWn5kGi9XrgDSGy-qfpVXhDXH43L_MlCqGxeohS5zRxSdTBrx7RfSeGvj6t9LXV8MncABDnaBjuPCNUC-LZ9-aIQlSq5lubk_m7MS4k2pDViZWTb3cHeMo72MdWipOE2thFmJr7B8s8ds_rkuYNdqVZQxDmFVnur2Qw36Nhu1iCbMMzqs_12fAssYJj23lbjaGfBEZYCsxC6WZ5b6A1PxveBOwiLXOoFKEy74IHq7-O_h-UkDgbGiMTk_0kZx41XKdBCO01WZ23trmoLTiUaMgkz3W5HwmgAAAAAg4MuhAA", None)
STRING2 = getenv("BQE_ZEYATWvqBtDyZRCUufkqmx_J7gXR6xL7p3p2pICljpNbMLKMI0hEL594tTWn5kGi9XrgDSGy-qfpVXhDXH43L_MlCqGxeohS5zRxSdTBrx7RfSeGvj6t9LXV8MncABDnaBjuPCNUC-LZ9-aIQlSq5lubk_m7MS4k2pDViZWTb3cHeMo72MdWipOE2thFmJr7B8s8ds_rkuYNdqVZQxDmFVnur2Qw36Nhu1iCbMMzqs_12fAssYJj23lbjaGfBEZYCsxC6WZ5b6A1PxveBOwiLXOoFKEy74IHq7-O_h-UkDgbGiMTk_0kZx41XKdBCO01WZ23trmoLTiUaMgkz3W5HwmgAAAAAg4MuhAA", None)
STRING3 = getenv("BQE_ZEYATWvqBtDyZRCUufkqmx_J7gXR6xL7p3p2pICljpNbMLKMI0hEL594tTWn5kGi9XrgDSGy-qfpVXhDXH43L_MlCqGxeohS5zRxSdTBrx7RfSeGvj6t9LXV8MncABDnaBjuPCNUC-LZ9-aIQlSq5lubk_m7MS4k2pDViZWTb3cHeMo72MdWipOE2thFmJr7B8s8ds_rkuYNdqVZQxDmFVnur2Qw36Nhu1iCbMMzqs_12fAssYJj23lbjaGfBEZYCsxC6WZ5b6A1PxveBOwiLXOoFKEy74IHq7-O_h-UkDgbGiMTk_0kZx41XKdBCO01WZ23trmoLTiUaMgkz3W5HwmgAAAAAg4MuhAA", None)
STRING4 = getenv("BQE_ZEYATWvqBtDyZRCUufkqmx_J7gXR6xL7p3p2pICljpNbMLKMI0hEL594tTWn5kGi9XrgDSGy-qfpVXhDXH43L_MlCqGxeohS5zRxSdTBrx7RfSeGvj6t9LXV8MncABDnaBjuPCNUC-LZ9-aIQlSq5lubk_m7MS4k2pDViZWTb3cHeMo72MdWipOE2thFmJr7B8s8ds_rkuYNdqVZQxDmFVnur2Qw36Nhu1iCbMMzqs_12fAssYJj23lbjaGfBEZYCsxC6WZ5b6A1PxveBOwiLXOoFKEy74IHq7-O_h-UkDgbGiMTk_0kZx41XKdBCO01WZ23trmoLTiUaMgkz3W5HwmgAAAAAg4MuhAA", None)
STRING5 = getenv("BQE_ZEYATWvqBtDyZRCUufkqmx_J7gXR6xL7p3p2pICljpNbMLKMI0hEL594tTWn5kGi9XrgDSGy-qfpVXhDXH43L_MlCqGxeohS5zRxSdTBrx7RfSeGvj6t9LXV8MncABDnaBjuPCNUC-LZ9-aIQlSq5lubk_m7MS4k2pDViZWTb3cHeMo72MdWipOE2thFmJr7B8s8ds_rkuYNdqVZQxDmFVnur2Qw36Nhu1iCbMMzqs_12fAssYJj23lbjaGfBEZYCsxC6WZ5b6A1PxveBOwiLXOoFKEy74IHq7-O_h-UkDgbGiMTk_0kZx41XKdBCO01WZ23trmoLTiUaMgkz3W5HwmgAAAAAg4MuhAA", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/214f53702f788c668e294.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STATS_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
STREAM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/214f53702f788c668e294.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
