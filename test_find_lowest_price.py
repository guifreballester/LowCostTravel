import unittest
from datetime import datetime

# Import the find_lowest_price function
from main import find_lowest_price

class TestFindLowestPrice(unittest.TestCase):
    def test_find_lowest_price(self):
        # Create a datetime object for the specific date
        specific_date = datetime(2023, 4, 10)

        # Define the minimum number of nights for the trip
        MIN_NIGHTS = 10

        # Define the maximum number of nights for the trip
        MAX_NIGHTS = 15

        # Define the price per night in euros
        PRICE_PER_NIGHT = 60

        # Define the price of flight to go per date as a dictionary
        # where the keys are dates in the format 'YYYY-MM-DD'
        # and the values are the prices in euros
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

        # Define the price of flight to come back per date as a dictionary
        # where the keys are dates in the format 'YYYY-MM-DD'
        # and the values are the prices in euros
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

        # Call the find_lowest_price function
        lowest_price, lowest_price_date = find_lowest_price(
            PRICE_OF_FLIGHT_TO_GO,
            PRICE_OF_FLIGHT_TO_COME_BACK,
            PRICE_PER_NIGHT,
            MIN_NIGHTS,
            MAX_NIGHTS
        )

        # Check if the lowest price is correct
        self.assertEqual(lowest_price, 770)

        # Check if the lowest price date is correct
        self.assertEqual(lowest_price_date, 'date_to_go: 2023-04-06 date_to_come_back: 2023-04-16')

# Run the test cases
if __name__ == '__main__':
    unittest.main()
