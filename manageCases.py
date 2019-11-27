"""
This script goes through files and directories to check for similar names.
CAT.txt and cat.txt are concidered the same name. It will add a copy number
to the end of the file: CAT-1.txt, cat-2.txt to make the names different in
each directory
"""
import os
import sys
from datetime import datetime as dt

# TODO: This doesn't work correctly the first time on the .thunderbird/../Imap
# files. Need to fix this before running it on next hard drive!

start_time = dt.now()
print('Started running: ', start_time)

if len(sys.argv) <= 1:
    print('Must enter path to scan')

path = sys.argv[1]

for root, dirs, files in os.walk(path):
	copy_num = 1  # Keep track of how many file names are the same
	lower = [f.lower() for f in files]
	for f in files:
		# remove file so it doesn't detect it
		cp = lower.copy()
		cp.remove(f.lower())
		if f.lower() in cp:
			loc = os.path.join(root, f)
			# check if f has an ending and add copy number for uniquness
			if '.' in f:
				start = '.'.join(f.split('.')[:-1]) + '-' + str(copy_num)
				end = f.split('.')[-1]
				f = '.'.join([start, end])
			else:
				f = f + '-' + str(copy_num)
			os.rename(loc, os.path.join(root, f))
			copy_num += 1

			print('***', loc) 
			print('*rename*', os.path.join(root, f))
			print('\n')	

	# check and rename directories
	lower =  [d.lower() for d in dirs]
	for d in dirs:
		cp = lower.copy()
		cp.remove(d.lower())
		if d.lower() in cp:
			loc = os.path.join(root, d)
			d = d + '-' + str(copy_num)
			os.rename(loc, os.path.join(root, d))
			copy_num += 1
			
			print('*****', loc)
			print('**Renamed**', os.path.join(root, d))
			print('\n')

end_time = dt.now()
print('Total runtime: ', str(end_time-start_time))
