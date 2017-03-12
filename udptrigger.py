#!/usr/bin/python
import ConfigParser, os, sys, socket
import subprocess

config = ConfigParser.ConfigParser()
config.read(sys.argv[1])


udp_ip = config.get("Network","ip")
udp_port = config.getint("Network","port")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind( (udp_ip,udp_port) )

cmds = config.items("Commands")

while True:
  data,addr = sock.recvfrom(128)
  print "received ",data

  for cmd in cmds:
    if cmd[0] in data:
      print subprocess.Popen(cmd[1],shell=True,stdout=subprocess.PIPE).stdout.read()
