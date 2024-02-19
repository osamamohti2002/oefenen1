import sys, os
from test_lib import test, report

basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(basepath)

expected = True
files = [
    'tha.py',
    'data.py',
    'functions.py',
    'test/run_all_tests.py',
    'test/test_O01.py',
    'test/test_lib.py',
]

for filepath in files:
    result = os.path.exists(basepath+'/'+filepath)
    test(filepath+' exsits',True, result)

if __name__ == "__main__":
    report()