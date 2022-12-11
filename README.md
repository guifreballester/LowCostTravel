# LowCostTravel

LowCostTravel is a tool for finding the best dates your next trip. It takes into account the prices of each flight plus the cost of the stay. Once you provide the number of days you can stay there, it will output the best date to start and end your trip.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or later

### Installing

1. Clone the repository:

```
git clone https://github.com/user/LowCostTravel.git
```

2. Install the required packages:

```
pip install -r requirements.txt
```

3. Run the program:

```
python main.py
```

## Usage

To use LowCostTravel, you need to provide the following information:

- The prices of flights to go, in the form of a dictionary with the date as the key and the price as the value
- The prices of flights to come back, in the form of a dictionary with the date as the key and the price as the value
- The average price per night for the hotel stay
- The minimum and maximum number of nights for the trip

For example:

```
PRICE_OF_FLIGHT_TO_GO = {'2022-12-01': 100, '2022-12-02': 120, '2022-12-03': 150}
PRICE_OF_FLIGHT_TO_COME_BACK = {'2022-12-10': 100, '2022-12-11': 120, '2022-12-12': 150}
PRICE_PER_NIGHT = 50
MIN_NIGHTS = 3
MAX_NIGHTS = 7

lowest_price, lowest_price_date = find_lowest_price(PRICE_OF_FLIGHT_TO_GO, PRICE_OF_FLIGHT_TO_COME_BACK, PRICE_PER_NIGHT, MIN_NIGHTS, MAX_NIGHTS)

print(f"The lowest price is {lowest_price} on {lowest_price_date}.")
```

This will find the most optimal dates for a trip that has a minimum of 3 nights and a maximum of 7 nights.

## Contributing
Please read [CONTRIBUTING.md](https://github.com/guifreballester/LowCostTravel/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
- [Guifré Ballester Basols] - Initial work - guifreballester

See also the list of [contributors](https://github.com/guifreballester/LowCostTravel/contributors) who participated in this project.

## License
This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/user/LowCostTravel/blob/master/LICENSE).
