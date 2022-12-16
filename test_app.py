from plantapp import supported_plants, your_table, program_plant_name_list, all_user_plant_data, plant_data, Plant

# TESTING Feature 1
# Expected Results: PASS
def test_plant_gets_added():
    add_plant = 'MONSTERA'
    if add_plant in supported_plants:
        your_table.add_row([add_plant])
        program_plant_name_list.append(add_plant)
    assert add_plant in supported_plants and program_plant_name_list and your_table

# TESTING Feature 1
# This test must be run with the succeding test 'commented out' as this test requires the plant collection to be removed to 0. 
# Expected Results: PASS
# To test, run pytest -s, then add a plant to your collection, remove that same plant, then skip to the end of app for results.
def test_table_and_list_length():
    remove_plant = 0    
    if remove_plant <= len(program_plant_name_list) and len(program_plant_name_list) > 0:
                your_table.del_row(int(remove_plant))
                program_plant_name_list.remove(program_plant_name_list[remove_plant])
    assert len(your_table.rows) == len(program_plant_name_list)
    assert len(your_table.rows) == 0
    assert len(program_plant_name_list) == 0
    
# TESTING Feature 4    
# This test must be run on it's own as it accepts user input while a plant exists in the 'collection'. Use pytest -s
# Expected Results: PASS
# To test, run pytest -s, then add a plant and make sure you select 'Y' for the 'is near window' question. 
def test_is_true_in_list_and_dict():
    for plant in program_plant_name_list:
        while True:
            add_location_data = 'Y'
            if add_location_data.upper() == 'Y': 
                plant_data.append(True)
                all_user_plant_data[plant].append((True))
                break  
assert plant_data[2] == True 
assert any(True in val for val in all_user_plant_data.values())

# TESTING Feature 4    
# This test must be run on it's own as it accepts user input while a plant exists in the 'collection'. Use pytest -s
# Expected Results: PASS
# To test, run pytest -s, then add a plant and make sure you select 'N' for the 'is near window' question. 
def test_is_false_in_list_and_dict():
    for plant in program_plant_name_list:
        while True:
            add_location_data = 'N'
            if add_location_data.upper() == 'N': 
                plant_data.append(False)
                all_user_plant_data[plant].append((False))   
                break
assert plant_data[2] == False
assert any(False in val for val in all_user_plant_data.values())      

