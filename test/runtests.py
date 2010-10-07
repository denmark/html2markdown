import unittest
import os
import sys
import glob

def main():
    # FIXME: relative path?
    sys.path.append(os.pardir + '/src')
    test_module_filenames = glob.glob('tests/test_*.py')
    test_modules = []
    for test_module in test_module_filenames:
        test_modules.append('tests.' + '.'.join(test_module.split(os.sep)[1:]).rstrip('.py'))

    suite = unittest.TestLoader().loadTestsFromNames(test_modules)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    sys.exit(main())
