# import necessary libraries
from datetime import datetime
import csv
import matplotlib.pyplot as plt

def get_datetime(date: str) -> datetime:
    """
    Convert a date in the format 'YYYY-MM-DD' to a datetime object.
    
    :param date: The date to convert to a datetime object
    :return: The date as a datetime object
    """
    return datetime.strptime(date, '%Y-%m-%d')

def get_num_nights(date_to_go: datetime, date_to_comeback: datetime) -> int:
    """
    Calculate the number of nights between two dates.
    
    :param date_to_go: The date to go on the trip
    :param date_to_comeback: The date to come back from the trip
    :return: The number of nights between the two dates
    """
    return (date_to_comeback - date_to_go).days

def get_trip_price(num_nights: int, price_per_night: int, price_to_go: int, price_to_comeback: int) -> int:
    """
    Calculate the total cost of a trip.
    
    :param num_nights: The number of nights for the trip
    :param price_per_night: The price per night for the trip
    :param price_to_go: The price of the flight to go
    :param price_to_comeback: The price of the flight to come back
    :return: The total cost of the trip
    """
    return num_nights * price_per_night + price_to_go + price_to_comeback

def find_lowest_price(PRICE_OF_FLIGHT_TO_GO, PRICE_OF_FLIGHT_TO_COMEBACK, PRICE_PER_NIGHT, MIN_NIGHTS, MAX_NIGHTS):
    total_cost = {}
    plot_data = []
    # iterate over the possible flight dates to go
    for date_to_go, price_to_go in PRICE_OF_FLIGHT_TO_GO.items():
        # convert the date to a datetime object
        date_to_go = get_datetime(date_to_go)
        price_to_go = int(price_to_go)

        # iterate over the possible flight dates to come back
        for date_to_comeback, price_to_comeback in PRICE_OF_FLIGHT_TO_COMEBACK.items():
            # convert the date to a datetime object
            date_to_comeback = get_datetime(date_to_comeback)
            price_to_comeback = int(price_to_comeback)

            # calculate the number of nights for the trip
            num_nights = get_num_nights(date_to_go, date_to_comeback)

            # check if the number of nights is greater than or equal to the minimum number of nights
            if num_nights >= MIN_NIGHTS and num_nights <= MAX_NIGHTS and date_to_comeback > specific_date:
                price = get_trip_price(num_nights, PRICE_PER_NIGHT, price_to_go, price_to_comeback)
                text = "date_to_go: "+date_to_go.strftime("%Y-%m-%d")+" date_to_comeback: "+date_to_comeback.strftime("%Y-%m-%d")
                total_cost[text] = price
                print(text, price)
                
                # create a dictionary
                plot_dictionary = {'date_to_go': date_to_go.strftime("%m-%d"), 'date_to_comeback': date_to_comeback.strftime("%m-%d"), 'price':price}
                
                # add the dictionary to the list
                plot_data.append(plot_dictionary)

    # Find the lowest price and its corresponding date
    lowest_price = min(total_cost.values())
    lowest_price_date = [date for date, price in total_cost.items() if price == lowest_price][0]
    
    # plot the data
    plot_prices(plot_data)

    # Return the lowest price and its date
    return lowest_price, lowest_price_date

def upload_prices_from_csv(csv_file_name: str) -> dict:
    # Create an empty dictionary
    prices = {}

    # Open the CSV file in read mode
    with open(csv_file_name, 'r') as csv_file:
        # Create a CSV reader
        reader = csv.reader(csv_file)

        # Iterate over the rows in the CSV file
        for row in reader:
            # Get the date and price from the row
            date, price = row

            # Add the date and price to the dictionary
            prices[date] = price

    # Return the dictionary
    return prices
    
def plot_prices(data):
    # create a list of x-values (date_to_go values)
    date_to_go_values = [datapoint["date_to_go"] for datapoint in data]
    # create a list of y-values (date_to_comeback values)
    date_to_comeback_values = [datapoint["date_to_comeback"] for datapoint in data]
    # create a list of z-values (price values)
    price_values = [datapoint["price"] for datapoint in data]

    # create a scatter plot with the x-values, y-values, and z-values
    plt.scatter(date_to_go_values, date_to_comeback_values, c=price_values)

    # add a colorbar to the scatter plot
    plt.colorbar()

    # show the plot
    plt.show()

# Create a datetime object for the specific date
specific_date = datetime(2023, 4, 10)

# define the minimum number of nights for the trip
MIN_NIGHTS = 9

# define the maximum number of nights for the trip
MAX_NIGHTS = 15

# define the price per night in euros
PRICE_PER_NIGHT = 60

if __name__ == '__main__':
    # define the price of flight to go and comeback per date as a dictionary
    # where the keys are dates in the format 'YYYY-MM-DD' and the
    # values are the prices of the flights for those dates
    csv_file_name_go = 'data/prices_go.csv'
    csv_file_name_comeback = 'data/prices_comeback.csv'
    
    # Upload the prices from the CSV file
    price_of_flight_to_go = upload_prices_from_csv(csv_file_name_go)
    price_of_flight_to_comeback = upload_prices_from_csv(csv_file_name_comeback)

    # Use the find_lowest_price() function to find the lowest price and its date
    lowest_price,lowest_price_date = find_lowest_price(price_of_flight_to_go, price_of_flight_to_comeback, PRICE_PER_NIGHT, MIN_NIGHTS, MAX_NIGHTS)
    
    # Print the lowest price and its date
    print(f"The lowest price is {lowest_price} on {lowest_price_date}.")
            
            
        
