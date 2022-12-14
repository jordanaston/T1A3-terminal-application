from plantapp import program_plant_name_list



def test_program_plant_name_list():
    program_plant_name_list[0] = 'MONSTERA'
    print(program_plant_name_list)
    # assert 'MONSTERA' in program_plant_name_list

# def test_will_pass():
#     assert 'hello' == 'hello'