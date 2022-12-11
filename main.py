# import necessary libraries
from datetime import datetime

def get_datetime(date: str) -> datetime:
    """
    Convert a date in the format 'YYYY-MM-DD' to a datetime object.
    
    :param date: The date to convert to a datetime object
    :return: The date as a datetime object
    """
    return datetime.strptime(date, '%Y-%m-%d')

def get_num_nights(date_to_go: datetime, date_to_come_back: datetime) -> int:
    """
    Calculate the number of nights between two dates.
    
    :param date_to_go: The date to go on the trip
    :param date_to_come_back: The date to come back from the trip
    :return: The number of nights between the two dates
    """
    return (date_to_come_back - date_to_go).days

def get_trip_price(num_nights: int, price_per_night: int, price_to_go: int, price_to_come_back: int) -> int:
    """
    Calculate the total cost of a trip.
    
    :param num_nights: The number of nights for the trip
    :param price_per_night: The price per night for the trip
    :param price_to_go: The price of the flight to go
    :param price_to_come_back: The price of the flight to come back
    :return: The total cost of the trip
    """
    return num_nights * price_per_night + price_to_go + price_to_come_back

# Create a datetime object for the specific date
specific_date = datetime(2023, 4, 10)

# define the minimum number of nights for the trip
MIN_NIGHTS = 10

# define the maximum number of nights for the trip
MAX_NIGHTS = 15

# define the price per night in euros
PRICE_PER_NIGHT = 60

# define the price of flight to go per date as a dictionary
# where the keys are dates in the format 'YYYY-MM-DD' and the
# values are the prices of the flights for those dates
PRICE_OF_FLIGHT_TO_GO = {
    '2023-03-27': 45,
    '2023-03-28': 70,
    '2023-03-29': 100,
    '2023-03-30': 110,
    '2023-03-31': 150,
    '2023-04-01': 140,
    '2023-04-02': 150,
    '2023-04-03': 150,
    '2023-04-04': 90,
    '2023-04-05': 120,
    '2023-04-06': 90,
    '2023-04-07': 150,
    '2023-04-08': 110,
    '2023-04-09': 100,
    '2023-04-10': 110,
    '2023-04-11': 110
}

# define the price of flight to come back per date as a dictionary
# where the keys are dates in the format 'YYYY-MM-DD' and the
# values are the prices of the flights for those dates
PRICE_OF_FLIGHT_TO_COME_BACK = {
    '2023-04-05': 90,
    '2023-04-06': 90,
    '2023-04-07': 170,
    '2023-04-08': 150,
    '2023-04-09': 150,
    '2023-04-10': 150,
    '2023-04-11': 180,
    '2023-04-12': 100,
    '2023-04-13': 140,
    '2023-04-14': 140,
    '2023-04-15': 80,
    '2023-04-16': 80,
    '2023-04-17': 100,
    '2023-04-18': 100,
    '2023-04-19': 165,
    '2023-04-20': 165,
    '2023-04-21': 120
}

# initialize a dictionary to store the total cost of the trip
# for each possible combination of dates
total_cost = {}

# iterate over the possible flight dates to go
for date_to_go, price_to_go in PRICE_OF_FLIGHT_TO_GO.items():
    # convert the date to a datetime object
    date_to_go = get_datetime(date_to_go)
    # print(date_to_go)

    # iterate over the possible flight dates to come back
    for date_to_come_back, price_to_come_back in PRICE_OF_FLIGHT_TO_COME_BACK.items():
        # convert the date to a datetime object
        date_to_come_back = get_datetime(date_to_come_back)
        # print(date_to_come_back)

        # calculate the number of nights for the trip
        num_nights = get_num_nights(date_to_go,date_to_come_back)
        # print(num_nights)

        # check if the number of nights is greater than or equal to the minimum number of nights
        if num_nights >= MIN_NIGHTS and num_nights <= MAX_NIGHTS and date_to_come_back > specific_date:
            price = get_trip_price(num_nights, PRICE_PER_NIGHT, price_to_go, price_to_come_back)
            text = "date_to_go: ",date_to_go.strftime("%Y-%m-%d"), "date_to_come_back: ", date_to_come_back.strftime("%Y-%m-%d")
            total_cost[text] = price

# Find the lowest price and its corresponding date
lowest_price = min(total_cost.values())
lowest_price_date = [date for date, price in total_cost.items() if price == lowest_price][0]

# Print the lowest price and its date
print(f"The lowest price is {lowest_price} on {lowest_price_date}.")
            
            
            