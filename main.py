#!/usr/bin/env python
# CS 340 Homework 01
# Flat Files & Physical Data
# Tyler Radabaugh

import sys
import csv
import operator

FIELD_NAMES = ['Transaction_date', 'Product', 'Price', 'Payment_Type', 'City', 'State', 'Country', 'Name', 'Account_Created', 'Last_Login', 'Latitude', 'Longitude']

if len(sys.argv) != 2:
	print "Useage: ./main.py your_csv_file.csv"
	exit(1)

SORT_BY_COLUMN_NUMBER = 1
csv_file_name = sys.argv[1]


# sorts csv data by given column number
def sort_data():
	with open (csv_file_name, 'r') as csv_file:
		reader =  csv.reader(csv_file, delimiter = ',')
		sorted_csv = sorted(reader, key = operator.itemgetter(SORT_BY_COLUMN_NUMBER))
		for row in sorted_csv:
			print ', '.join(row)


# prints a count of the number of customers named "Amanda"
def count_amandas():
	number_of_amandas = 0

	with open(csv_file_name, 'r') as csv_file:
		reader = csv.reader(csv_file, delimiter = ',')
		for row in reader:
			for field in row:
				if isinstance(field, basestring):
					if "amanda" in field.lower():
						number_of_amandas += 1


	print ("The file contains %(number_of_amandas)i customers named Amanda." % locals())


sort_data()
count_amandas()