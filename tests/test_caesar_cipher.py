from  caesar_cipher.caesar import encrypt ,decrypt ,crack


def test_encrypt():
    expected = 'wi xkwo sc webkn kvurkdsl'
    actual = encrypt('My name is Murad Alkhatib', 10)
    assert actual == expected

def test_decrypt():
    expected = 'hello'
    actual = decrypt('Gdkkn', 25)
    assert actual == expected 

def test_crack():
    assert crack("kjkjkd") == None

def test_crack2():
    output = "it was the best of times, it was the worst of times."
    assert crack("Yj mqi jxu ruij ev jycui, yj mqi jxu mehij ev jycui.") == output



    