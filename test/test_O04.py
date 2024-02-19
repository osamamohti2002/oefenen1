import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

#schrijf je test hier
expected = 2
result = 2
test('JOURNEY_IN_DAYS - test 1',expected, result)



if __name__ == "__main__":
    report()