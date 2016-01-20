# vision.extract
# Extracts financial information from Finances.xlsx and writes them to CSVs.
#
# Author:   Benjamin Bengfort <bengfort@cs.umd.edu>
# Created:  Wed Dec 02 20:41:22 2015 -0500
#
# Copyright (C) 2015 University of Maryland
# For license information, see LICENSE.txt
#
# ID: extract.py [] benjamin@bengfort.com $

"""
Extracts financial information from Finances.xlsx and writes them to CSVs.
"""

##########################################################################
## Imports
##########################################################################

import os
import csv

from datetime import datetime
from vision.reader import SpreadsheetReader

##########################################################################
## Module Constants
##########################################################################

PROJECT  = os.path.dirname(os.path.dirname(__file__))
FINANCES = os.path.join(PROJECT, "fixtures", "Finances.xlsx")
ACCOUNTS = os.path.join(PROJECT, "fixtures", "accounts.csv")
TRANSACT = os.path.join(PROJECT, "fixtures", "transactions.csv")

MONTH    = "%b%y"

ACT_FLDS = [
    u'Month', u'Account Type', u'Bank', u'Account Name', u'Beginning Balance', u'Ending Balance',
]

TRN_FLDS = [
    u'Month', u'Date', u'Amount', u'From Account', u'To Account'
]

##########################################################################
## Extraction
##########################################################################

def extract(finances=FINANCES, accounts=ACCOUNTS, transact=TRANSACT):
    """
    Reads the sheets from finances and writes out the accounts and
    transactions to the correct locations.
    """

    reader   = SpreadsheetReader(finances)
    with open(accounts, 'w') as af:
        with open(transact, 'w') as tf:
            act_writer = csv.DictWriter(af, ACT_FLDS)
            trn_writer = csv.DictWriter(tf, TRN_FLDS)

            act_writer.writeheader()
            trn_writer.writeheader()

            for month in reader.sheets:
                if month.lower() == 'blank': continue

                try:
                    sheet = reader.finances(month)

                    for a in sheet.accounts:
                        a['Month'] = sheet.date
                        act_writer.writerow(a)

                    for t in sheet.transactions:
                        t['Month'] = sheet.date
                        trn_writer.writerow(t)
                except Exception as e:
                    print "{}: {}".format(month, e)


if __name__ == '__main__':
    extract()
