#!/usr/bin/python

import urllib2
import lxml.html
import csv
import pymssql
from datetime import datetime

def getCSV(link,conn):
	filename = '/tmp/'+link[0].replace(" ","")+'.csv'
	print filename

	f = open(filename, "wb")
	f.write(urllib2.urlopen(link[1]).read())
	f.close()

	reader = csv.reader(open(filename,'rb'))
	cur = conn.cursor()
	for row in reader:
		cur.execute("INSERT INTO ODSdata (\
						OrganisationCode,OrganisationName,NationalGroupingCode,\
						HighLevelHealthAuthority, AddressLine1,AddressLine2,AddressLine3,AddressLine4,\
						AddressLine5,PostCode,OpenDate,CloseDate,filename,rowadded) VALUES \
						(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )",\
						(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],\
						filename,datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
	conn.commit()


response = urllib2.urlopen('http://www.connectingforhealth.nhs.uk/systemsandservices/data/ods/datafiles')
html = response.read()
root = lxml.html.fromstring(html) 
data = []

for el in root.cssselect("table.listing a"):
	if 'csv' in el.attrib['href']:
		data.append([el.attrib['title'],el.attrib['href']])

conn = pymssql.connect(host='HOSTNAME', user='USERNAME', password='PASSWORD', database='DATABASE')

for link in data:
	getCSV(link,conn)

conn.close()