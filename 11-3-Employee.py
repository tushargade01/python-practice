from employee import Employee

def test_give_default_raise():
    emply = Employee('tushar','gade', 50_000)
    emply.give_raise()
    assert emply.salary == 55_000


def test_give_custome_raise():
    emply = Employee('tushar','gade', 50_000)
    emply.give_raise(10_000)
    assert emply.salary == 60_000


test_give_default_raise()
test_give_custome_raise()