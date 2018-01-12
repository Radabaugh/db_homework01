#!/usr/bin/env python
# CS 340 Homework 01
# Flat Files & Physical Data
# Tyler Radabaugh

import sys
import csv
import operator

if len(sys.argv) != 2:
	print "Useage: ./main.py your_csv_file.csv"
	exit(1)

SORT_BY_COLUMN_NUMBER = 1
csv_file_name = sys.argv[1]


def open_file():
	file = []
	with open (csv_file_name, 'r') as csv_file:
		reader =  csv.reader(csv_file, delimiter = ',')
		for row in reader:
			file.append(row)
	return file


# sorts csv data by given column number
def sort_data():
	sorted_csv = sorted(open_file(), key = operator.itemgetter(SORT_BY_COLUMN_NUMBER))
	for row in sorted_csv:
		print ', '.join(row)


# prints a count of the number of customers named "Amanda"
def count_amandas():
	number_of_amandas = 0

	for row in open_file():
		for field in row:
			if "amanda" in field.lower():
				number_of_amandas += 1

	print ("The file contains %(number_of_amandas)i customers named Amanda." % locals())


# returns the mean of a list of numbers
# https://stackoverflow.com/questions/7716331/calculating-arithmetic-mean-average-in-python
def mean(numbers):
	return float(sum(numbers)) / max(len(numbers), 1)


# prints the avarage transaction amount
def average_transaction():
	row_count = 0
	transaction_prices = []

	for row in open_file():
		if row_count > 0:
			field_count = 0
			for field in row:
				field_count += 1
				if field_count == 3 and field:
					transaction_prices.append(float(field))
		row_count += 1

	average_transaction_price = mean(transaction_prices)
	print ("The average transaction price is $%(average_transaction_price)f" % locals())


sort_data()
count_amandas()
average_transaction()
