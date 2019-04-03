#coding:utf-8
#python3

import socket
import time


def  scan(ip,port):
	try:
		socket.setdefaulttimeout(3)
		s=socket.socket()
		s.connect((ip,port))
		return True
	except:
		
		return False
	
def scanPort():
	print("------------ip端口扫描----------------")
	print("------------适用真实ip----------------")
	ip=input("请输入IP")
	#socket.sethostbyname(”xx.com“)  可以获取主机IP 
	startTime=time.time()
	for port in range(21,6565):
		
		res=scan(ip,port)

		if res:
			print("this port:%s is on",port)
	endTime=time.time()
	print("本次扫描用了%s秒",endTime-startTime)
	
if __name__ =='__main__':
	scanPort()