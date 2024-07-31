# ARBROKER
#### Video Demo: https://youtu.be/U6mvqisamxc
#### Description:

Arbroker is a Python software that gives you the action's price of the 100 most important companies in real-time.
Also, it gives you the conversion of the action's price in eur/dollar in real-time.
But that's not all. Arbroker gives you the price of that action you choose in a period of time you also choose, following the change percentage of that day, using the compound interest formula.

Arbroker software is composed of two files: project.py and dictionary.py.

The Project.py file is the main file, where you can find all functions used in the software for extracting real-time data using APIs.
In project.py you also find other functions used for printing the final output, applying the compound interest formula, and more.

Finally, in project.py you will find the main function, where all the program is executed and coordinated for printing and giving to the user the precise data and information he/she wants.

In the other file, called dictionary.py, we find a full dictionary composed for the names of the 100 most valued companies in the world and their API TOKEN, for accessing their market-value information in real time.

This dictionary.py is used for printing at the start of the program all the options the user has for receiving data, but also for connecting to the API, using its API TOKEN, and finally, is used at the final printing output, for knowing based on the API TOKEN the user has inputted, what company is, and then printing its name.

For extracting the real-time data, Arbroker connects with finnhub.io API for extracting the market-value information of every company, and for extracting the real-time difference between Euro (€) and Dollar ($), Arbroker uses exchangegenerate-api.com API.

When the project.py file is executed, it prints all the 100 most important companies in the world and their API TOKEN and then prompts the user for an API TOKEN.

If the user doesn't input a valid API token, the program will quit using sys.exit with an error message: "INVALID API token.".

If the user inputs a correct API token, the program will prompt again for a period of time in days for calculating the action price at the end of that time period. This number of days will be used for calculating the action price at the end of that time period, using the compound interest formula.

For successfully applying the compound interest formula, Arbroker uses the funcion get_data for extracting the price action, change percentage and the date from the API.

The development of Arbroker was difficult in general, but the hardest part was applying the API's extraction information methods and finding real-time information for applying it in the execution of the program.

Finally, for making prettier all the code files, I used Black formatter to unify all the code syntax and make it easier when reading the code.

This is how my final project works. I believe Arbroker can be a useful tool for some basic operations in investing and for finding information about some actions and their price, as well as their position in the stock market.
