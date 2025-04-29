# Telegram Language Translation Bot

This is a simple Telegram bot that translates messages sent by users from any language to English using Google Translate API.

## Steps to Run:

1. Clone the repository to your local machine or server.
2. Create a new bot on Telegram using [BotFather](https://core.telegram.org/bots#botfather) and get the API token.
3. Add the API token as an environment variable or directly in the `bot.py` file.
4. Install the required dependencies by running:
    ```bash
    pip install -r requirements.txt
    ```
5. Start the bot by running:
    ```bash
    bash start.sh
    ```

The bot will reply with the translated text when you send a message.

## Requirements:
- Python 3.x
- Telegram Bot API Token
- Google Translate API via googletrans package

## Deployment:
You can deploy this bot on platforms like [Railway](https://railway.app) for automatic hosting.

