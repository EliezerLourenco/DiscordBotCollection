# Python Discord Bot Collection

This repository contains a collection of Discord bots written in Python, showcasing different functionalities using the Discord API.

## Bots Included

- `discordListMembers.py`: Lists all members of a specified Discord guild when the bot starts.
- `discordOnReady.py`: Logs a message when the bot connects to a guild and responds to mentions in chat.
- `timeBot.py`: Handles timezone-related commands, providing a list of timezones and current times.
- `welcomeBot.py`: Sends welcome messages to new members in a guild channel and via direct message.

## Setup

To get these bots up and running:

1. Install the required packages: pip install discord.py python-dotenv aiohttp


2. Set up your `.env` file with the following contents, replacing the placeholder text with your actual details: DISCORD_TOKEN=your_bot_token_here
DISCORD_GUILD=your_guild_name_here

3. Execute any bot script with Python. For example: python discordListMembers.py


## Features

- **Member Listing**: The bot fetches and displays a list of all guild members.
- **Connection Status**: Notifies in the console when the bot is connected to the Discord guild.
- **Time Zone Queries**: Users can request a list of timezones or the current time in a specified timezone.
- **Welcoming New Members**: Automatically sends a greeting to new members joining the guild.

## Contributing

Feel free to fork this repository, make your changes, and create a pull request with your improvements.

## License

This project is released under the MIT License - see the [LICENSE](LICENSE.md) file for details.


