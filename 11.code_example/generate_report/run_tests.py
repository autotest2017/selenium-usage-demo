#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
download page: http://tungwaiyip.info/software/HTMLTestRunner.html
"""
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner


class TestMountain(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_it_is_true(self):
        self.assertTrue(1 == 0)
        print "fail..."
        #self.assertTrue(1 != 0)

    def test_it_is_false(self):
        self.assertFalse(1 == 0)
        print "success..."

    def test_single_quote_strings(self):
        self.assertTrue('aaa' == "aaa")

    def test_strip_strings(self):
        self.assertTrue("  aaa   ".strip() == "aaa")
        self.assertTrue("  aaa".lstrip() == "aaa")
        self.assertTrue("aaa   ".rstrip() == "aaa")


class TestMain(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_if_else(self):
        if True:
            assert 1 == 1
        else:
            assert 1 != 1


def fun_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(TestMain('test_if_else'))
    suite.addTest(TestMountain('test_it_is_true'))
    suite.addTest(TestMountain('test_it_is_false'))
    #suite.addTests(loader.loadTestsFromTestCase(TestMountain))
    return suite

if __name__ == '__main__':
    #res = unittest.TextTestRunner(verbosity=2).run(fun_suite())

    fp = open('./test_result_%s.html' % time.strftime("%Y-%m-%d %H-%M-%S"), 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'测试报告生成范例',
                            description=u"测试用例执行情况：")
    runner.run(fun_suite())
    fp.close()
    sys.exit(0)
