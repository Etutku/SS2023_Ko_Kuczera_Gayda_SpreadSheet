'''
Working on it
'''

import pytz
CEST = pytz.timezone('Eurioe/Warsaw')
software_version = 'v1.1'

def update_clock():
    raw_TS = datetime.now(CEST)
    now = raw_TS.strftime("%a, %H:%M:%S%p")
    label_date_time.config(text = now)
    label_date_time.after(1000, update_clock)

update_clock()
