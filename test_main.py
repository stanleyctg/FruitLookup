import json
import pytest
from main import FruitLookup

# Fetch fruits once for test parameterization
fruits = FruitLookup.fetch_all_fruits()
if fruits is None:
    raise Exception("Failed to fetch fruits from the API for test parameterization.")

@pytest.mark.parametrize("fruit", fruits)
def test_fetch_fruit(fruit):
    '''Test fetching fruit data from the API against the full list'''
    fruit_name = fruit.get('name')
    fruit_lookup = FruitLookup(fruit_name)
    fruit_data = fruit_lookup.get_fruit()
    assert fruit_data == fruit, f"Failed for {fruit_name}"

@pytest.mark.parametrize("fruit", fruits)
def test_human_readable_output(capsys, fruit):
    '''Test human-readable output for each fruit, ensuring all fields are printed'''
    fruit_lookup = FruitLookup(fruit.get("name"))
    fruit_lookup.human_readable_output(fruit)

    # Capture the printed output.
    captured_output = capsys.readouterr().out
    
    # Extract the expected fields.
    expected_name = fruit.get("name")
    expected_id = fruit.get("id")
    expected_family = fruit.get("family")
    nutritions = fruit.get("nutritions", {})
    expected_sugar = nutritions.get("sugar")
    expected_carbs = nutritions.get("carbohydrates")
    
    # Assert that the printed output contains the expected values.
    for key, expected in [
        ("Name", expected_name),
        ("ID", expected_id),
        ("Family", expected_family),
        ("Sugar", expected_sugar),
        ("Carbohydrates", expected_carbs)
    ]:
        assert str(expected) in captured_output, f"Printed output does not contain '{expected}' for {key}"

@pytest.mark.parametrize("fruit", fruits)
def test_machine_readable_output(capsys, fruit):
    '''Test machine-readable output for each fruit, ensuring all fields are printed'''
    fruit_lookup = FruitLookup(fruit.get("name"), output_format="machine")
    fruit_lookup.machine_readable_output(fruit)
    
    # Capture the printed output.
    captured_output = capsys.readouterr().out
    output_json = json.loads(captured_output)
    
    # Extract expected values.
    expected_name = fruit.get("name")
    expected_id = fruit.get("id")
    expected_family = fruit.get("family")
    nutritions = fruit.get("nutritions", {})
    expected_sugar = nutritions.get("sugar")
    expected_carbs = nutritions.get("carbohydrates")
    
    # Assert that the output JSON contains the expected values.
    assert output_json["Full Name"] == expected_name, f"Expected name {expected_name}"
    assert output_json["ID"] == expected_id, f"Expected ID {expected_id}"
    assert output_json["Family"] == expected_family, f"Expected family {expected_family}"
    assert output_json["Sugar"] == expected_sugar, f"Expected sugar {expected_sugar}"
    assert output_json["Carbohydrates"] == expected_carbs, f"Expected carbohydrates {expected_carbs}"