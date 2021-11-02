from  caesar_cipher.caesar import encrypt ,decrypt ,crack


def test_encrypt():
    expected = 'Wi xkwo sc Webkn Kvurkdsl'
    actual = encrypt('My name is Murad Alkhatib', 10)
    assert actual == expected

def test_decrypt():
    expected = 'My name is Murad Alkhatib'
    actual = decrypt('Wi xkwo sc Webkn Kvurkdsl', 10)
    assert actual == expected 

def test_crack():
    assert crack('Wi xkwo sc Webkn Kvurkdsl') == 'My name is Murad Alkhatib'