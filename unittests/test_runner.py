import unittest
import calc_tests

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(calc_tests.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)