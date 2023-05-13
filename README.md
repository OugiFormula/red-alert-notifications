# Red Alert Notifications

This small python script will use windows 10 & 11 notifications to give you alerts about missiles.

## Getting Started

You need to make sure you have the right libraries installed from the requirements.txt file.

You can do so by:

1. cd to the directory where requirements.txt is located.
2. activate your virtualenv.
3. run: ```pip install -r requirements.txt``` in your shell.

If you want to set it up for specific cities you can do so by changing the lines from
```
tzevaadom.alerts_listener(handlerhe) 
```
To
```
tzevaadom.alerts_listener(handlerhe,alerts_only_for_cities=["עיר א","עיר ב"])
```
make sure on both hebrew and english you wrote the city names in hebrew.

### Prerequisites

before using the program please make sure you have the following.

* Python 3
* Libraries mentioned in the requrements.txt file

## Q&A

* Q) Can I take the code and make a product of my own using your Class?
* Absolutely. The code and everything inside the repository is open-sourced. The Code is under MIT license - please make sure to understand the meaning. The Code provided AS IS WITHOUT ANY WARRANTY.

