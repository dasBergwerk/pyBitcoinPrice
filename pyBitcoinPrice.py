#!/usr/bin/python2

import urllib2
import json

anfrage = urllib2.Request('https://api.coindesk.com/v1/bpi/currentprice/EUR.json')
antwort = urllib2.urlopen(anfrage)
seite = antwort.read()
datei = open('daten.json','wb')
datei.write(seite)
datei.close()

parsed_json = json.loads(seite)

print (parsed_json['time']['updatedISO'])
print (parsed_json['bpi']['EUR']['rate'])
