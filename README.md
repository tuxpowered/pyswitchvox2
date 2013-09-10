pyswitchvox2
============

Python class to interface with Digium Switchvox

A collection of Class wrappers to expose the Digium API for Switchvox. 

Issues related to previously referenced pyswitchvox with submitting some JSON payloads. 

Some of this code is based on pyswitchvox work, I have updated the methods to use the Requests package which is not only easier to read (as a human) but also hides a lot of the complexity and confusion of urllib/urllib2 and httplib/httplib2.

In the future I hope to expose more sub-classes directly. 

Additionally this project will (hopefully) end up having an AMI mappings, to allow developers to write common code for asterisk, and switchvox.

I welcome feed back and input.



Usage:

from switchvox import Switchvox

sv = Switchvox()
sv.hostname = 'demo.server.tld'
sv.user_name = '100'
sv.user_pass = 'Sup3rSeret'
method = 'switchvox.users.getMyInfo'
parameters = {}

r = sv.request(method, parameters)

r.json()

r.text
