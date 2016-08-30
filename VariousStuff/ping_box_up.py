#!/bin/env python

import os 
import sys
import smtplib
from email.mime.text import MIMEText

def mailto(to_addr, message, subject='', from_addr='colin.bernet@cern.ch'):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    s = smtplib.SMTP('localhost')
    s.sendmail(from_addr, [to_addr], msg.as_string())
    s.quit()

def action_up():
    mailto('colin.bernet@cern.ch', '', '{ip} is up!'.format(ip=hostname) )

def action_down():
    addrs = ['colin.bernet@cern.ch',
             'colin.bernet@gmail.com']
    if hostname == ip_bernet:
        addrs.append('bertrandmolinier@yahoo.fr')
    for addr in addrs: 
        mailto(addr, 
               '''
Salut Bertrand, 

Pourrais-tu relever le disjoncteur s'il te plait? 
Merci!

Colin et Maud.
''',
               'Alerte: coupure de courant chez les Bernet!', 

)


ip_bernet = '88.175.213.86' # bernet bervilliere
hostname = ip_bernet
if len(sys.argv)==2:
    hostname = sys.argv[1]

response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print hostname, 'is up!'
  action_up()
else:
  print hostname, 'is down!'
  action_down()

