# Chia-Bot

## Description

The __Chia-Bot__ is a useful tool that is helpful for those who are farming Chia crypto currency. This is an easily configurable Discord bot, which features several functions that present useful data about the user's Chia farm, wallet, or plotting operation. The bot allows a Discord user to send messages to the bot and receive a response with the desired information.

## Usage

The __Chia Bot__ needs to be running on the same machine as your Chia operations (Chia blockchain and plotting operations). To begin using the bot you will need to configure a few settings so the bot can collect information about your Chia applications, and so it can communicate with your Discord webhook(s). Configuration is described in the section below and is crucial for the bot to work properly.

You'll also need to add the bot to your Discord server. This process requires serveral steps, so I recommend you follow a tutorial like [this one.](https://www.selecthub.com/resources/how-to-add-bots-to-discord/) 

Once the bot is configured it is time to start the bot. Open a new command prompt in the directory of the Chia Bot. Then run the _chia_bot.py_ file using a Python command such as `python3 chia_bot.py` or `py chia_bot.py`. After a moment you'll see a message saying the user has connected to Discord.

## Configuration

The __Chia Bot__ requires some basic configuration to work for the individual user. Additionally, it provides some options that customize the usage of tools. Settings and configuration are handled in a _config.yaml_ file. To create this file - copy the _config.yaml.default_ file and then rename it to _config.yaml_ for user configuration. *DO NOT MAKE CHANGES TO THE DEFAULT FILE. ONLY MAKE CHANGES TO YOUR NEW CONFIG FILE*

Once you have created the new configuration file, you may begin changing parameters to suit your needs. Here are descriptions of the necessary and unnecessary parameters:

### Notifications

Notifications are sent to Discord webhooks. You may use the same webhook for multiple parameters, or different ones based on how you would like notifications delivered.

* __system_webhook__ - The Discord webhook where notifications where "System Monitoring" notifications will sent.
* __plotter_webhook__ - The Discord webhook where notifications where "Plotter Monitoring" notifications will sent.
* __miner_webhook_true__ - The Discord webhook where notifications where "Miner Monitoring" notifications will sent if recurring notifications are set.
* __miner_webhook_false__ - The Discord webhook where notifications where "Miner Monitoring" notifications will sent only if the miner is not running.

### System Parameters

Use these settings to confugire how the system monitor runs. You may need to change these parameters several times to find the threshhold which works best for you.

* __always_notify__ - If False - it will only notify the plot manager is not running or a threshhold is broken.
* __cpu_high__ - Will notify if it exceeds this threshhold (in percent)
* __cpu_low__ - Will notify if below this threshhold (in percent)
* __ram_high__ - Will notify if it exceeds this threshhold (in percent)
* __ram_low__ - Will notify if below this threshhold (in percent)

### Plotting Parameters

Use this setting to configure how the plotter monitor runs.

* __pslog_path__ - The folder where the PSChiaPlotter logs are located - __MUST BE SET.__  Example: _C:\Users\CurrentUser\.chia\mainnet\plotter_

### Miner Parameters

Use these settings to configure how the miner monitor runs.

* __always_notify__ - If False - it will only notify if a mining process is not running.
* __hpool_path__ - The folder where your HPOOL Miner is located. - __MUST BE SET.__ Example: _C:\Users\CurrentUser\Documents\HPool-Miner-chia-v1.4.1-0-windows_
* __chia_path__ - The folder where your Chia.exe is located. - __MUST BE SET.__ Example: _C:\Users\CurrentUser\AppData\Local\chia-blockchain\app-1.2.2\resources\app.asar.unpacked\daemon_


## Commands

If everything is correctly configured and the bot has been started, then it is time to begin sending it commands. From your Discord channel you may begin sending the bot commands. For a command to work it must use a prefix of a dollar sign ("$"). Here are a list of commands, followed by an explanation of how they work.
* __clear__ - Deletes a certain amount of messages from the channel - use syntax `$clear 5`
* __wallet__ - Chia Bot will return a message containing the current balance of your Chia wallet, and will notify you if you have new Chia coin - use syntax `$wallet`
* __farm__ - Chia Bot will return a message containing information about your Chia farm, including the size (in TiB) of the farm and number of plots - use syntax `$farm`
* __plotter__ - Chia Bot will return a message telling you if your plotter is or is not running - use syntax `$plotter`
* __price__ - Chia Bot will return the current price of the crypto currency of your choice. This is not just limited to Chia, but can be used for most cryptocurrencies - use syntax `$price Chia` or `price BTC`
