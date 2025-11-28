import project

def test_search():
    project.add("sanam", "9812345678")
    assert project.search("sanam") == "9812345678"
    assert project.search("manas") == None

def test_check_name():
    assert project.check_name("sanam") == True
    assert project.check_name("5@n@m") == False

def test_check_phone():
    assert project.check_phone("9812345678") == True
    assert project.check_phone("98") == False