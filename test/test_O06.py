import sys, os
from test_lib import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import friends
from functions import getFromListByKeyIs

expected = 6
result = len(friends)
test('friends imported', expected, result)

testarg_list_alltests = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]

expected = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'round', True)
test('getFromListByKeyIs - test 1',expected, result)


expected = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Soccerball',
        'tasty' : False,
        'round' : True
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'round', True)
test('getFromListByKeyIs - test 2',expected, result)


expected = [{
        'name' : 'Pie',
        'tasty' : True,
        'round' : True
    },{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'tasty', True)
test('getFromListByKeyIs - test 3',expected, result)


expected = [{
        'name' : 'Fries',
        'tasty' : True,
        'round' : False
    }]
result = getFromListByKeyIs(testarg_list_alltests, 'round', False)
test('getFromListByKeyIs - test 4',expected, result)


expected = []
result = getFromListByKeyIs(testarg_list_alltests, 'name', 'notExistingValue')
test('getFromListByKeyIs - test 5',expected, result)


expected = []
result = getFromListByKeyIs(testarg_list_alltests, 'notExistingKey', '?')
test('getFromListByKeyIs - test 6',expected, result)


if __name__ == "__main__":
    report()
