#!/usr/bin/python

import sys

highest_sales = {}

for line in sys.stdin:
    data = line.strip().split("\t")
    date, time, store, item, cost, payment = data

    if len(data) != 6:
        continue

    if payment in highest_sales:
        highest_sales[payment] = max(highest_sales[payment], float(cost))
    else:
        highest_sales[payment] = float(cost)
        
for payment, sale in highest_sales.items():
    print(payment+": "+str(sale))
