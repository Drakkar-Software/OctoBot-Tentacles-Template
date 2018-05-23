# CryptoBot-Package-Template
This repository contains the template for custom packages handled by CryptoBot's package manager.

# How to use it ?

* Add any Evaluator, Strategy or Util function in the appropriate folder
  * Evaluators can be using: 
    * Technical Analysis (TA folder)
    * Social analysis (Social folder) 
    * RealTime analysis (RealTime folder)
* Add the following header on top of this newly create module:
```
"""
CryptoBot Package

$package_description: {
    "name": "module_name",
    "type": "module_type",
    "version": "module_version",
    "requirements": []
}
"""
```
Here is a header example from the default package forum_evaluator download by default by CryptoBot and available [here](https://github.com/Trading-Bot/CryptoBot-Packages/blob/master/Social/forum_evaluator.py):
```
"""
CryptoBot Package

$package_description: {
    "name": "forum_evaluator",
    "type": "Social",
    "version": "1.0.0",
    "requirements": []
}
"""
```
* Run generate.py : this will create a packages_list.json file using the module header. This file is used by CryptoBot to handle the package.

Your package is now ready to be installed. 
To install it, add the url to a GitHub repository containing the package (or the local path to the package) in **config/config.json** inside the **"packages"** part.

Example:
```
"packages": [
    "C:/Users/JohnSmith/TradingBots/Advanced-Trading-Package"
  ],
```
You can add as many packages as you want, just separate them with a **","**.

They will be automatically installed when running the command:
```
python start.py -p install all
```
It is also possible to specify which module(s) to install by naming it(them). In this case only the modules available in the available packages can be installed.
```
python start.py -p install forum_evaluator john_smith_macd_evaluator advanced_twitter_evaluator
```

Do no hesitate to propose your new modules to the CryptoBot comunity !