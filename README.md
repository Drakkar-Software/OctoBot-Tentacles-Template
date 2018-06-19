# OctoBot-Tentacles-Template [![Build Status](https://api.travis-ci.org/Drakkar-Software/OctoBot-Tentacles-Template.svg?branch=master)](https://travis-ci.org/Drakkar-Software/OctoBot-Tentacles-Template)
This repository contains the template for custom tentacles packages handled by [OctoBot](https://github.com/Drakkar-Software/OctoBot)'s tentacle manager.

# How to use it ?

* Add any Evaluator, Strategy, Util function or trading mode in the appropriate folder
  * Evaluators can be using: 
    * Technical Analysis (TA folder)
    * Social analysis (Social folder) 
    * RealTime analysis (RealTime folder)
* Add the following header on top of the created tentacle:
```
"""
OctoBot Tentacle

$tentacle_description: {
    "name": "tentacle_name",
    "type": "tentacle_type",
    "subtype": "tentacle_sub_type",
    "version": "tentacle_version",
    "requirements": ["required_tentacle_name", "another_required_tentacle_name==specific_tentacle_version"],
    "config_files": ["tentacle_configuration_file_name"],
    "tests": ["tentacle_test_file_1", "tentacle_test_file_2"]
}
"""
```
* **name**: Name of the tentacle (name of the file)
* **type**: Type of the tentacle (Evaluator or Trading)
* **subtype**: Sub-type of the tentacle (type of Evaluator or Trading: Social, TA, Mode, ...)
* **version**: Version of the tentacle with a 3 number format (1.0.2, 15.1.215, ...)
* **requirements**: Optional: List of required tentacles for this tentacle (identified by tentacle name between **""** and separated by a **,**.
* **config_files**: Optional: List of configuration files for this tentacle (identified by file name between **""** and separated by a **,**). These files are stored next to the tentacle file in a tentacles package and are installed in the **config** folder of the associated tentacle's subtype when the package is installed by [OctoBot](https://github.com/Drakkar-Software/OctoBot)'s tentacle manager.
* **tests**: Optional: List of tests for this tentacle (identified by test file name between **""** and separated by a **,**).

Here is a header example from the default tentacle forum_evaluator download by default by OctoBot and available [here](https://github.com/Drakkar-Software/OctoBot-Tentacles/blob/master/Social/forum_evaluator.py):
```
"""
OctoBot Tentacle

$tentacle_description: {
    "name": "forum_evaluator",
    "type": "Evaluator",
    "subtype": "Social",
    "version": "1.0.0",
    "requirements": [],
    "config_files": ["RedditForumEvaluator.json"]
}
"""
```
Another example with tests included (available [here](https://github.com/Drakkar-Software/OctoBot-Tentacles/blob/master/Trading/Mode/daily_trading_mode.py)): 
```
OctoBot Tentacle

$tentacle_description: {
    "name": "daily_trading_mode",
    "type": "Trading",
    "subtype": "Mode",
    "version": "1.0.0",
    "requirements": [],
    "tests":["test_daily_trading_mode_creator", "test_daily_trading_mode_decider"]
}
```
* Run `generate.py` : this will create a **tentacles_list.json** file using the module header. This file is used by OctoBot to handle tentacles package.

Your tentacle is now ready to be installed. 
To install it, add the url to a [GitHub](https://github.com/) repository containing the tentacle (or the local path to the tentacle) in **config.json** inside the **"tentacles"** part.

Example:
```
"tentacles": [
    "C:/Users/JohnSmith/TradingBots/Advanced-Trading-Tentacles"
  ],
```
You can add as many tentacles (packages) as you want, just separate them with a **","**.

They will be automatically installed when running the command:
```
python start.py -p install all
```
It is also possible to specify which module(s) to install by naming it(them). In this case only the modules available in the available tentacles can be installed.
```
python start.py -p install forum_evaluator john_smith_macd_evaluator advanced_twitter_evaluator
```

**Do not hesitate to propose your new modules to the OctoBot comunity !**
