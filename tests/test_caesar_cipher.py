from  caesar_cipher.caesar import encrypt ,decrypt ,crack


def test_encrypt():
    expected = 'Wi xkwo sc Webkn Kvurkdsl '
    actual = encrypt('My name is Murad Alkhatib', 10)
    assert actual == expected

def test_decrypt():
    expected = 'Hello '
    actual = decrypt('Gdkkn', 25)
    assert actual == expected 

def test_crack():
    assert crack("kjkjkd") == None