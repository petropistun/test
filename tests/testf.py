import os, sys
import logging, logging.handlers
import time
from pprint import pprint

import pexpect


def test_1():
        assert 5 == 1, "Message 2222222222"



child = pexpect.spawn('python ./tests/test.py')
time.sleep(30)

#test_1()


