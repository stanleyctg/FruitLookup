# FruitLookup

Program that allow user to search information about a specific fruit.

## Description:

     In 'main.py' file, it consists the implementation that adheres to the specifications and requirements. In the 'test_main.py' file consists the implmentation of test cases for functions in main.

## Dependancies:

    Install requests and pytest to run both application and test file.

## Usage:

### Command Line:

    Run the script:
        [python/python3] main.py [fruit name] -f/--f [human, machine]
    example of searching for an apple
        [python/python3] main.py apple -f human
        [python/python3] main.py apple -f machine

        OR

        [python/python3] main.py apple --format human
        [python/python3] main.py apple --format machine

    Additional details about usage can be found by this script:
        [python/python3] main.py -h

### Library function:

    - Import the class 'FruitLookup' from main into a seperate program.
    - Initialise the class with these parameters (fruit_name, human/machine)
    - Finally invoke the run() method from the class
    Example of searching for an apple:
        FruitLookup("apple", "machine").run()

        OR

        FruitLookup("apple", "human").run()
