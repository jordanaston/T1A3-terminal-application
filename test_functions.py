from plantapp import supported_plants



def test_supported_plants(plant):
    
    assert plant in supported_plants

supported_plants('MONSTERA')