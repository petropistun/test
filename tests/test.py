import os, sys
import logging, logging.handlers
import time

from pprint import pprint



i = 0
while 1:
	print ".", i
	file = open('out', 'a')
	file.write(" i = %d\n"%i)
	file.close()
	time.sleep(1)
	i += 1
	if i > 60:
		break



print "====end="
