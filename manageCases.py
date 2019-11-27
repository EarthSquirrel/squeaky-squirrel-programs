import os
import sys

if len(sys.argv) <= 1:
    print('Must enter path to scan')

path = sys.argv[1]

for root, dirs, files in os.walk(path):
	lower = [f.lower() for f in files]
	for f in files:
		cp = lower.copy()
		cp.remove(f.lower())
		if f.lower() in cp:
			print('***', os.path.join(root, f)) 
			print('\n')	
