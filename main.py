import requests
import argparse
import json

# API URL
API_URL = 'https://www.fruityvice.com/api/fruit'

class FruitLookup:
    def __init__(self, fruit_name, output_format='human'):
        self.fruit_name = fruit_name
        self.output_format = output_format

    def get_fruit(self):
        '''Fetch fruit data from API'''
        try:
            response = requests.get(f'{API_URL}/{self.fruit_name.lower()}')
            if response.status_code == 200:
                return response.json()
        except Exception as e:
            print(f"Error fetching data {e}")
        return None

    def human_readable_output(self, fruit_data):
        '''Print human-readable output'''
        print(f"Full Name: {fruit_data.get('name')}")
        print(f"ID: {fruit_data.get('id')}")
        print(f"Family: {fruit_data.get('family')}")
        print(f"Sugar: {fruit_data.get('nutritions').get('sugar')}g")
        print(f"Carbohydrates: {fruit_data.get('nutritions').get('carbohydrates')}g")

    def machine_readable_output(self, fruit_data):
        '''Print machine-readable output'''
        output = {
            "Full Name": fruit_data.get("name"),
            "ID": fruit_data.get("id"),
            "Family": fruit_data.get("family"),
            "Sugar": fruit_data.get("nutritions").get("sugar"),
            "Carbohydrates": fruit_data.get("nutritions").get("carbohydrates"),
        }
        print(json.dumps(output, indent=4))

    def run(self):
        '''Method to fetch and display fruit data'''
        fruit_data = self.get_fruit()
        if fruit_data is None:
            print(f"Fruit '{self.fruit_name}' not found")
            return
        if self.output_format == 'machine':
            self.machine_readable_output(fruit_data)
        else:
            self.human_readable_output(fruit_data)


if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Fruit lookup using Fruityvice API'
    )
    parser.add_argument('Fruit', help="Name of the fruit to look up (e.g., 'Strawberry', 'Banana')")
    parser.add_argument(
        '-f', '--format',
        choices=['human', 'machine'],
        default='human',
        help="Choose output format: 'human' for human-readable output, 'machine' for JSON format."
    )
    args = parser.parse_args()
    lookup = FruitLookup(args.Fruit, args.format)
    lookup.run()