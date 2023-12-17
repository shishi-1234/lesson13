from functions import salary, hello_who
def test_hello_who_max():
    assert hello_who('Max') == 'hello,Max'
    assert hello_who('Maria') == 'hello,Maria'
    assert hello_who('Leo') == 'hello,Leo'
    assert hello_who('Peter') == 'hello,Peter'
    assert hello_who('Lera') == 'hello,Lera'
def tesr_salary():
    assert(2,2) != 8
    assert (3,1) != 6