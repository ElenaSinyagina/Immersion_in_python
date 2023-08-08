import Task
import unittest

class testDate(unittest.TestCase):

    def testDays(self):
        text = "21.11.2001"
        self.assertEqual(True, Task.funcDate(text))
       # self.assertEqual(False, Task.funcDate(text))  
        self.assertEqual(False, Task.funcDate("32.11.2000"))

import pytest
myList = [1, 9, 5, 3, 2]
def sortList(myList):
    resList = sorted(myList)
    return resList

def testList():
    assert [1, 2, 3, 5, 9] == sortList(myList)