from plantapp import supported_plants, your_table, program_plant_name_list
# from prettytable import PrettyTable


def test_supported_plants():
    plant = 'MONSTERA'
    assert plant in supported_plants

def test_get_started():
    add_plant = 'MONSTERA'
    if add_plant in supported_plants:
        your_table.add_row([add_plant])
        program_plant_name_list.append(add_plant)
    assert add_plant in supported_plants and program_plant_name_list and your_table

def test_update_plant_collection():
    while True:
            try:
                remove_plant = 0
                break
            except ValueError:
                print("\nINVALID SELECTION! Please select 'A' (ADD Plant), 'R' (Remove Plant) or 'F' (Finalise Collection)\n")
    if remove_plant <= len(program_plant_name_list) and len(program_plant_name_list) > 0:
                your_table.del_row(int(remove_plant))
                program_plant_name_list.remove(program_plant_name_list[remove_plant])
    assert len(your_table.rows) == len(program_plant_name_list)
    
            
