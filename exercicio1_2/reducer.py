#!/usr/bin/python
import sys

sales_totals = {}

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        continue

    this_key, this_sale = data

    if this_key in sales_totals:
        sales_totals[this_key] += float(this_sale)
    else:
        sales_totals[this_key] = float(this_sale)

for this_key, total in sales_totals.items():
    print(this_key+": "+str(total))
