def test_import():
    from icdmappings.mappers import ICD9toLEVEL3
    return

def test_init():
    from icdmappings.mappers import ICD9toLEVEL3
    mapper = ICD9toLEVEL3()
    return 

def test_mapper():
    
    from icdmappings.mappers import ICD9toLEVEL3
    mapper = ICD9toLEVEL3()

    code = ""
    expected = None
    result = mapper.map(code)
    assert result is expected

    code = "123.45"
    expected = "123"
    result = mapper.map(code)
    assert result == expected

    code = 2.45
    expected = None
    result = mapper.map(code)
    assert result is expected

    code = ["abcd", 123, "75849", ""]
    expected = ["abc", None, "758", None]
    result = mapper.map(code)
    assert result == expected