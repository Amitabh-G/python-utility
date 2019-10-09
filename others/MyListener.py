# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 12:08:43 2018

@author: amitabh.gunjan
"""

import time
import sys
import stomp
import json

class Listener(stomp.ConnectionListener):
    def __init__(self, conn):
        self.conn = conn

conn1 = stomp.Connection12(host_and_ports = None)
conn1.set_listener(name = 'QLIB_Processor_Listener_printer',  lstnr = Listener(conn1))
conn1.start()
conn1.connect(username = 'admin', passcode = 'admin', wait = True)
conn1.subscribe(destination = 'test', id = 1, ack = 'auto')  
inpt = [{
                "asset": "CBOT Wheat",
                "exType": "European",
                "optionType": "Call",
                "strikePrice": 100.9901,
                "expiryDate": "03/12/2018",
                "valueDate": "04/11/2018",
                "volatility": 0.109987,
                "riskFreeRate": 0.020019,
                "underlyingPrice": 99.9901,

                "longShort": "Long",
                "premium" : 0.10            
},
{
                "asset": "CBOT Maize",
                "exType": "European",
                "optionType": "Put",
                "strikePrice": 100.9901,
                "expiryDate": "03/12/2018",
                "valueDate": "04/11/2018",
                "volatility": 0.109987,
                "riskFreeRate": 0.020019,
                "underlyingPrice": 99.9901,

                "longShort": "Long",
                "premium" : 0.10
}]

inpt_str = json.dumps(inpt)

conn1.send('test',inpt_str )
conn1.disconnect()


#class MyListener(stomp.ConnectionListener):
#    def __init__(self, conn):
#        self.conn = conn
##    pass
#    
#    def on_error(self, headers, message):
#        print('received an error "%s"' % message)
#        
#    def on_message(self, headers, message):
#        
#        print('receive a message "%s"' % message)
#        print('message is :', message)
#        json_message = json.dumps(message)
#        print('json_message',json_message)
#        print(json_message.split(':'))
#
#        try:
#            input_data = json.loads(json_message)
#            print('input_data is:', input_data)
#            print(input_data[0])
#            num = input_data[1]
#        except:
#            raise(ValueError)
#        return(input_data)
###        
#
##conn = stomp.Connection([('192.168.1.66', 61613)])
#conn = stomp.Connection12(host_and_ports = None)
#
#conn.set_listener(name = 'QLIB_Processor_Listener', lstnr =  MyListener(conn))
#conn.start()
#conn.connect(username = 'admin', passcode = 'admin', wait = True)
#conn.subscribe(destination = 'test', id = 1, ack = 'auto')
#print('Connected...waiting...')

#while True:
#    pass


#print('Disconnecting...')
#conn.disconnect()
#conn1.disconnect()
#print('Disconnected')





