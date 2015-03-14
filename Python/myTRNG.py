## Other misterious code...

# -*- coding: utf-8 -*-
import time
import binascii

data = ''
for n in range(1000000):
	time1 = time.clock()
	time2 = time.time()
	string = str(time1*time2)[-4:]
	if "." not in string:
		#data.append(string)

		# to convert into 0 and 1
		binary = bin(int(binascii.hexlify(string)))
		data += binary
		#data.append(binary[2:])
print data
		
		

# single_string = ''
# for item in data:		
# 	single_string += item
#print single_string

fod = open("numbers.bin", "ab")
fod.write(data)
fod.close()