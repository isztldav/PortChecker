#!/usr/bin/env python
from socket import * 

if __name__ == '__main__':
	target = raw_input('Enter host to scan: ')
    	targetIP = gethostbyname(target)
    	print 'Starting scan on host ', targetIP
    	array = ['21','25','80','139','3389','1723','1521','23','110','445','8080','5900','1433','3306']
    	arrayname = ['FTP','SMTP','HTTP','NETBIOS','RDP','VPN','Oracle DB','TELNET','POP3','Windows file Sharing','firewall','VNC','MSQL','Mysql']
    	#scan reserved ports
    	for i in range(0,len(array)):
        	s = socket(AF_INET, SOCK_STREAM)
		s.settimeout(1)
        	result = s.connect_ex((targetIP, int(array[i])))

        	if(result == 0) :
            		print "Port", array[i], arraynname[i], "OPEN"
		else:
			print "Port", array[i], arrayname[i], "CLOSE"
        	s.close()
