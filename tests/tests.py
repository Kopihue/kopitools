from kopitools.args import (
    Registry, Args,
    EntryPointNotFoundError, ArgError
)
import sys

def get_voice_options() -> Args | None:
    try:
        voice = Registry(sys.argv, "voice")
    except EntryPointNotFoundError:
        return None

    return voice.collect()

def get_chat_options() -> Args | None:
    try:
        chat = Registry(sys.argv, "chat")
    except EntryPointNotFoundError:
        return None

    chat.option(
        "--flush",
        receives=None,
        default=False,
        attribute="flush",
    )

    return chat.collect()

def get_main_options() -> Args:
    main = Registry(sys.argv)

    main.option(
        "--llm-model",
        receives=str,
        default="gemma4",
        attribute="llm_model"
    )
    main.option(
        "--num-ctx",
        receives=int,
        default=8192,
        attribute="num_ctx",
    )

    return main.collect()

main = get_main_options()
chat, voice = get_chat_options(), get_voice_options()
action = None

if chat is not None and voice is not None:
    print("You can only choose one action!")
    sys.exit(1)

elif chat is None and not voice is None:
    print("You gotta choose an action!")
    sys.exit(1)

action = chat if chat is not None else voice

if action is None:
    sys.exit(1)

print(main._args)
print("=" * 50)
print(action._args)
