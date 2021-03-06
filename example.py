#!/usr/bin/python

from ADIF_log import ADIF_log
import datetime
import os

# Create a new log...
log = ADIF_log('Py-ADIF Example')
entry = log.newEntry()

# New entry from K6BSD to WD1CKS
entry['OPerator'] = 'K6BSD'
entry['Call'] = 'WD1CKS'
entry['QSO_Date']=datetime.datetime.now().strftime('%Y%m%d')
entry['baNd']='20M'
entry['mODe']='PSK'
entry['SubMode']='PSK31'
entry['TIME_ON']=datetime.datetime.now().strftime('%H%M')
entry['comment_intl']=u'Testing... \xb0'

# Write to example.adif
f = open('example.adif', 'wt')
f.write(str(log))
f.close()

# Write to example.adx
f = open('example.adx', 'wt')
f.write(log.xml())
f.close()

# Read example.adif back...
newlog = ADIF_log('Py-ADIF Example', file='example.adif')
print newlog[0]['CALL'],' band: ',newlog[0]['BAND']

# Read example.adx back...
newlog = ADIF_log('Py-ADIF Example', file='example.adx')
print newlog[0]['call'],' band: ',newlog[0]['band']

# Clean up... nothing interesting here...
os.remove('example.adif')
os.remove('example.adx')
