# OctoBot Tentacle Template
This repository contains the template for custom tentacles (packages) handled by [OctoBot](https://github.com/Drakkar-Software/OctoBot)'s tentacle manager.

# How to use it ?

* Add any Evaluator, Strategy or Util function in the appropriate folder
  * Evaluators can be using: 
    * Technical Analysis (TA folder)
    * Social analysis (Social folder) 
    * RealTime analysis (RealTime folder)
* Add the following header on top of this newly create module:
```
"""
OctoBot Tentacle

$tentacle_description: {
    "name": "module_name",
    "type": "module_type",
    "version": "module_version",
    "requirements": []
}
"""
```
Here is a header example from the default tentacle forum_evaluator download by default by OctoBot and available [here](https://github.com/Drakkar-Software/OctoBot-Tentacles/blob/master/Social/forum_evaluator.py):
```
"""
OctoBot Tentacle

$tentacle_description: {
    "name": "forum_evaluator",
    "type": "Social",
    "version": "1.0.0",
    "requirements": []
}
"""
```
* Run generate.py : this will create a tentacles_list.json file using the module header. This file is used by OctoBot to handle the tentacle (package).

Your tentacle is now ready to be installed. 
To install it, add the url to a GitHub repository containing the tentacle (or the local path to the tentacle) in **config/config.json** inside the **"tentacles"** part.

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
