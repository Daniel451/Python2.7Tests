import timeit
from DummyArithmetic import DA


class CIT(object):

    @staticmethod
    def test_time():
        dao = DA() 
        dao.calc()

        T = timeit.Timer(dao.calc)
        T.timeit(number=int(1e8))


CIT.test_time()
