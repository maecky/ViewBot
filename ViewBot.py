#!/usr/bin/python
import pycurl
import time
import sys

print
print "dP     dP oo                      888888ba             dP   "
print "88     88                         88    `8b            88     by j0eblack"
print "88    .8P dP .d8888b. dP  dP  dP a88aaaa8P' .d8888b. d8888P "
print "88    d8' 88 88ooood8 88  88  88  88   `8b. 88'  `88   88   "
print "88  .d8P  88 88.  ... 88.88b.88'  88    .88 88.  .88   88   "
print "888888'   dP `88888P' 8888P Y8P   88888888P `88888P'   dP   "
print
class Storage:
    def __init__(self):
        self.contents = ''
        self.line = 0

    def store(self, buf):
        self.line = self.line + 1
        self.contents = "%s%i: %s" % (self.contents, self.line, buf)

    def __str__(self):
        return self.contents

retrieved_body = Storage()
retrieved_headers = Storage()
link=raw_input("Enter url: ")
try:
	link = str(link)
	if len(link)<=5:
		sys.exit()
except:
	print "Invalid url."
	sys.exit()
fopen=open('prox.txt','r')
popen=open('port.txt','r')
count=sum(1 for line in open('prox.txt'))
print
print "Proxy List Loaded." 
def view():
	while True:
		try:
			line=fopen.next()
			port=popen.next()
			c1=pycurl.Curl()
			c1.setopt(pycurl.URL, '%s'%link)
			c1.setopt(pycurl.WRITEFUNCTION, retrieved_body.store)
			c1.setopt(pycurl.HEADERFUNCTION, retrieved_headers.store)
			c1.setopt(pycurl.PROXY, '%s'%line)
			c1.setopt(pycurl.PROXYPORT, int(port))
			c1.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS4)
			c1.perform()
			time.sleep(2)
			print "View done with proxy: %s"%line
		except StopIteration:
			print
			print "End of proxy list."
			sys.exit()
def start():
	for i in range(count):
		view()
start()
