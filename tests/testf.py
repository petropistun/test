import os, sys
import logging, logging.handlers
import time
import subprocess
from pprint import pprint

import pexpect


def test_1():
        assert 5 == 1, "Message 2222222222"



print "===begin==="
child = pexpect.spawn('python ./tests/test.py')



import subprocess
#process = subprocess.Popen(['ps', 'aux'],  shell=True, stdout=subprocess.PIPE)
#out, err = process.communicate()
subprocess.call("ps ax | grep python", shell=True)

#print("Processs=====", out)
#print("Processs err=====", err)

time.sleep(10)

file = open('out', 'r')

print "out begin>>>>>"
print file.read()
print "<<<<out end"


print "===end==="

#test_1()


