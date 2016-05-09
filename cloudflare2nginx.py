"""
@authors: Rafael Tovar <hola AT rafaeltovar.info>

This script write a full config file for nginx
for accept only connections from Cloudflare servers.

TODO write how to
"""

OUTPUT_FILE = "cloudflare.conf"

# from # https://www.cloudflare.com/ips
CLOUDFLARE_IPv4 = "https://www.cloudflare.com/ips-v4"
CLOUDFLARE_IPv6 = "https://www.cloudflare.com/ips-v6"

import time, urllib2

# get cloudflare ips
contentIPv4 = urllib2.urlopen(CLOUDFLARE_IPv4).read()
contentIPv6 = urllib2.urlopen(CLOUDFLARE_IPv6).read()


# write file
# TODO control permission?
f = open(OUTPUT_FILE,'w')
f.write('# By Cloudflare2Nginx script\n')
f.write('# UPDATE: ' + time.strftime("%d/%m/%Y")+'\n\n')
f.write('# IPv4\n')
for line in contentIPv4.splitlines():
  f.write('allow ' + line + ';\n')

f.write('\n# IPv6\n')
for line in contentIPv6.splitlines():
  f.write('allow ' + line + ';\n')

f.write('# Deny all petition\n')
f.write('deny all;\n')
f.close()
