# CheapFlightsFinder

CheapFlightsFinder is a tool for finding the lowest prices for flights.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.6 or later

### Installing
1. Clone the repository:

```git clone https://github.com/user/CheapFlightsFinder.git```

Install the required packages:
Copy code
pip install -r requirements.txt
Run the program:
Copy code
python main.py
Usage
To use CheapFlightsFinder, you need to provide the following information:

The prices of flights to go, in the form of a dictionary with the date as the key and the price as the value
The prices of flights to come back, in the form of a dictionary with the date as the key and the price as the value
The price per night for the hotel
The minimum and maximum number of nights for the trip
For example:

Copy code
PRICE_OF_FLIGHT_TO_GO = {'2022-12-01': 100, '2022-12-02': 120, '2022-12-03': 150}
PRICE_OF_FLIGHT_TO_COME_BACK = {'2022-12-10': 100, '2022-12-11': 120, '2022-12-12': 150}
PRICE_PER_NIGHT = 50
MIN_NIGHTS = 3
MAX_NIGHTS = 7

lowest_price, lowest_price_date = find_lowest_price(PRICE_OF_FLIGHT_TO_GO, PRICE_OF_FLIGHT_TO_COME_BACK, PRICE_PER_NIGHT, MIN_NIGHTS, MAX_NIGHTS)

print(f"The lowest price is {lowest_price} on {lowest_price_date}.")
This will find the lowest price for a trip that has a minimum of 3 nights and a maximum of 7 nights.

Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

Authors
[Your Name] - Initial work - Your GitHub username
See also the list of contributors who participated in this project.

License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/user/CheapFlightsFinder/blob/master/LICENSE.