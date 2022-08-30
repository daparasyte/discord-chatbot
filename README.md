# Discord Chatbot
This bot is built using [neuralintents](https://github.com/NeuralNine/neuralintents) - a simple interface for working with intents and chatbots. (It uses a sequential neural network model)


## Creating Discord Bot:
1. Go to: [Discord Developer Portal](https://discord.com/developers/application)
2. Click "New Application" and give your bot a name
3. Click "Bot" under settings on the left side of the screen
4. Click "Add Bot", then click "Yes, do it!"
(If you want the token of yout bot, click "Copy" under "TOKEN")
5. To add the bot to your server, click "OAuth2" under settings
6. Select "bot" under "SCOPES" and click "Copy" on the bottom right
7. Now paste the link you copied in your browser, select the server then click "Authorize"

Your bot is now ready.


## Installing Dependencies:
```
pip install discord
pip install python-dotenv
pip install neuralintents
```

## Usage:
Paste your Discord Bot Token and Discord channel ID in the `.env` file and execute the script.

Once you get - `"bot_name" is running...`, tag the bot in order to get responses to your messages.
