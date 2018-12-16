import sys
from score_word import score_word

if len(sys.argv) < 2:
	print("Please provide a Scrabble rack")
	exit(1)
print("here")
rack = sys.argv[1]
if len(rack) <2 or len(rack) >7:
	print("Please provide a Scrabble rack between 2 and 7 characters")
	exit(1)

rack = rack.lower()
print(rack)

with open("sowpods.txt","r") as infile:
	raw_input = infile.readlines()
	data = [datum.strip('\n').lower() for datum in raw_input]

output = []
for sowpod in data:
	flag = 1 ## assume each character in sowpod is in rack, init flag=1
	rack_cp = list(rack)
	wildcard = ''
	for char in sowpod:
		if char not in rack_cp: ## if one char not in rack
			wildcard += char
			if '*' in rack_cp:  ## try to use wildcard
				rack_cp.remove('*')
			elif '?' in rack_cp:
				rack_cp.remove('?')
			else:
				flag = 0 ## if any char is not in rack, break loop with flag=0
				break
		else:
			rack_cp.remove(char)
	if flag == 1:
		s = score_word(sowpod)
		if wildcard != '':
			s -= score_word(wildcard)
		output.append((s, sowpod))

output.sort(reverse = True)

for row in output:
	print(row)

