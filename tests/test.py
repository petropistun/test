import os, sys
import logging, logging.handlers
import time

from pprint import pprint


file = open('README.md', 'r')

print file.read()
i  = 0
while 1:
	print ".", i
	time.sleep(1)
	i += 1
	if i > 60:
		break

print "====end="
