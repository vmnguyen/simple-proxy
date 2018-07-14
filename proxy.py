#! /usr/bin/python
import socket, sys
from thread import *


#Colors and shit like that
white = '\033[97m'
green = '\033[92m'
red = '\033[91m'
yellow = '\033[93m'
end = '\033[0m'
back = '\033[7;91m'
info = '\033[93m[!]\033[0m'
que = '\033[94m[?]\033[0m'
bad = '\033[91m[-]\033[0m'
good = '\033[32m[+]\033[0m'
run = '\033[97m[~]\033[0m'

listening_port = 8889
max_connection = 5
buffer_size = 8192


def start():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(('', listening_port))
		s.listen(max_connection)
		print "[*] Initilizing Sockets ... Done"
		print "[*] Sockets Binded Successfully ..."
		print "[*] Server Started Successfully in port [%d] \n" % (listening_port)
	except Exception, e:
		print "[*] Unable to Initilize Socket"
		print e
		sys.exit(2)
	while 1:
		try:
			conn, addr = s.accept()
			data = conn.recv(buffer_size)
			print data
			print conn
			start_new_thread(conn_string, (conn, data, addr))
		except KeyboardInterrupt:
			s.close()
			print "\n Proxy Server Shutting Down ... "
			print "[*] Good bye"
			sys.exit(1)
	s.close()


# e.g: genk.vn vs http://genk.vn
# 		
def conn_string(conn, data, addr):	
	try:
		first_line = data.split('\n', 0)
		# first_line may look like this: GET http://genk.vn/ HTTP/1.1
		url  = first_line.split(' ', 1)

		http_pos = url.find("://")
		if http_pos == -1:
			temp = url
		else:
			temp = url[http_pos+3:]
		slash_pos = temp.find('/')
		temp2 = ""
		if slash_pos == -1:
			temp2 = temp
		else:
			temp2 = temp[:slash_pos]

		comma_pos = temp2.find(':') 
		if comma_pos == -1:
			port = 80
		else:
			port = temp[comma_pos:]
		print port
	except Exception, e: 
		print e
		pass
start()