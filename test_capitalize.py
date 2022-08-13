def capitalize_string(s):
    if not isinstance(s, str):
        raise TypeError('Please provide a string')
    return s.capitalize()

def sum(s, num, num2):
    result = num + num2
    return result    

def test_capitalize_string():
    assert capitalize_string('test') == 'Test'