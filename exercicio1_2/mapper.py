#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

sales_totals = {}

for line in sys.stdin:
	data = line.strip().split("\t")
	date, time, store, item, cost, payment = data

	if len(data)!=6:
		continue
  
	if item in sales_totals:
		sales_totals[item] += float(cost)
	else:
		sales_totals[item] = float(cost)

for item, total in sales_totals.items():
    print(item+": "+str(total))
