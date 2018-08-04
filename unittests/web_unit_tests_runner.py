import unittest
import web_unit_tests
import calc_tests

webTestSuite = unittest.TestSuite()
webTestSuite.addTest(unittest.makeSuite(web_unit_tests.PythonOrgSearch))
webTestSuite.addTest(unittest.makeSuite(calc_tests.CalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(webTestSuite)