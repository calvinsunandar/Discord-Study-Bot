Python Discord Study Bot
=========

This is a simple study timer bot for Discord that helps users manage their study sessions by providing reminders to take breaks. The bot uses Discord commands to start and end study sessions, and it sends messages at predefined intervals to remind users to take breaks.

Features
--------

-   **Start a study session**: Start tracking time for a study session.
-   **Break reminders**: Automatically remind the user to take a break after a specified period of study time (default: 30 minutes).
-   **End a study session**: End the current study session and display the total study time.
-   **Graceful bot shutdown**: Allows the bot to be manually shut down with a command.

Prerequisites
-------------

1.  **Python 3.7+**: Make sure you have Python installed. You can download it from [here](https://www.python.org/downloads/).
2.  **Discord.py library**: Install the required libraries using pip:

    ```pip install discord.py```

4.  **pytz library**: Install the `pytz` library for handling timezones:

    ```pip install pytz```

Setup Instructions
------------------

1.  **Clone the repository** (if using version control) or copy the script to your local environment.

2.  **Create a Discord bot**:

    -   Go to the Discord Developer Portal.
    -   Create a new application and add a bot to it.
    -   Copy the bot token from the Bot settings.
3.  **Update the bot token**:

    -   Replace the `BOT_TOKEN` variable in the script with your bot's token:

       ```BOT_TOKEN = "Insert Your Bot Token Here"```

4.  **Set your Discord channel ID**:

    -   Right-click the channel you want the bot to interact with and copy the channel ID.
    -   Replace the `CHANNEL_ID` variable in the script:

        ```CHANNEL_ID = "Insert Your Channel ID Here"```

5.  **Customize the time zone**:

    -   Set your desired time zone using `pytz`. The current script uses `America/Chicago`, but you can change it based on your location:

        ```local_tz = pytz.timezone('America/Chicago')```

    -   You can find a list of available time zones [here](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
6.  **Set the session time**:

    -   You can customize the maximum session time before a break reminder by adjusting the `MAX_SESSION_TIME_MINUTES` variable:

        ```MAX_SESSION_TIME_MINUTES = 30```

How to Use
----------

1.  **Start the bot**: Run the script in your terminal:

    ```python bot.py```

3.  **Commands**:

    -   `!start`: Start a new study session. The bot will record the start time and notify the user when the session begins.
    -   `!end`: End the current study session. The bot will calculate and display the total session duration in hours, minutes, and seconds.
    -   `!shutdown`: Gracefully shuts down the bot, with a "Goodbye" message.
4.  **Break Reminder**:

    -   The bot will remind users to take a break after the specified study time (default: 30 minutes).
    -   If the bot runs for more than one session, reminders will continue until the session is ended.

Example Usage
-------------

-   **Start a study session**:

    `User: !start
    Bot: New session started at 10:45:30 AM!`

-   **Break reminder** (after the session runs for 30 minutes):

    `Bot: Time to take a break! You've been studying for 30 minutes.`

-   **End a study session**:

    `User: !end
    Bot: Session ended after 0 hours, 45 minutes, 30 seconds!`

-   **Shutdown the bot**:

    `User: !shutdown
    Bot: Goodbye! Shutting down now...`

Notes
-----

-   Make sure the bot has the necessary permissions in your Discord server to send messages in the specified channel.
-   You can adjust the time intervals for the break reminder by changing `MAX_SESSION_TIME_MINUTES`.

License
-------

This project is open-source and free to use.
