from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.type import AuthScope, ChatEvent
from twitchAPI.chat import Chat, EventData, ChatMessage, ChatSub, ChatCommand
import asyncio

from browser import translate_text, translate_text_2


APP_ID = 'i1rcrdwcobohu098fkcq0xqmxmgj26'
APP_SECRET = '9az0xj99r5eee59iykhhomew4n31nv'

# TARGET_CHANNEL = ['rostislav_999', 'w33haa', 'recrent']
TARGET_CHANNEL = ['worick_4']
# TARGET_CHANNEL = ['tpabomah']
USER_SCOPE = [AuthScope.CHAT_READ, AuthScope.CHAT_EDIT]
USERNAME = 'shivajreddy',
ACCESS_TOKEN = 'm29orn1hzua9uqekexdn22va36qawb'
OAUTH = 'oauth:m29orn1hzua9uqekexdn22va36qawb'


# event handler:: triggers when READY
async def on_ready(ready_event: EventData):
    print("✅ Bot is ready")
    await ready_event.chat.join_room(TARGET_CHANNEL)


# event handler when the channel gets a new message
async def on_message(msg: ChatMessage):
    # print(f'{msg.user.name}: {msg.text}')
    # msg_in_english = translate_text(msg.text)
    msg_in_english = translate_text_2(msg.text)
    # print(f'converted: ${converted}')
    print(f"{msg.user.name}: {msg_in_english}")


# set up the bot
async def run():

    twitch = await Twitch(app_id=APP_ID, app_secret=APP_SECRET)
    print(f'twitch: ${twitch}')

    auth = UserAuthenticator(twitch, USER_SCOPE)
    print('auth: ', auth)

    token, refresh_token = await auth.authenticate()
    # token, refresh_token = await auth.authenticate(user_token=ACCESS_TOKEN)
    print(f"token:${token} refresh_token:${refresh_token}")

    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # chat instance
    chat = await Chat(twitch)

    print("chat:", chat)

    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)
    print("☑️ events registered")

    print('chat about to start')
    chat.start()

    try:
        input('press ENTER to stop\n')
    finally:
        chat.stop()
        await twitch.close()

# Run the bot
asyncio.run(run())
