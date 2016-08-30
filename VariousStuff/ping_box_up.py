#!/bin/env python

import os 
import sys
import smtplib
from email.mime.text import MIMEText

def mailto(to_addr, message, subject='', from_addr='colin.bernet@cern.ch'):
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = ', '.join(to_addr)
    s = smtplib.SMTP('localhost')
    s.sendmail(from_addr, to_addr, msg.as_string())
    s.quit()

def action_up():
    mailto(['colin.bernet@cern.ch', 'colin.bernet@gmail.com'], 
           '', '{ip} is up!'.format(ip=hostname) )

def action_down():
    addrs = ['colin.bernet@cern.ch',
             'colin.bernet@gmail.com']
    if hostname == ip_bernet:
        addrs.extend([
                'bertrandmolinier@yahoo.fr',
                'petitemaud@gmail.com'])
    msg = '''
Salut Bertrand, 

Pourrais-tu relever le disjoncteur s'il te plait? 
Merci!

Colin et Maud.
'''
    subject = 'Alerte: coupure de courant chez les Bernet!'
    # for addr in addrs: 
    #     mailto(addr, msg, subject)
    mailto(addrs, msg, subject)


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

