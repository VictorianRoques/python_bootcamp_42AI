import sys
data = sys.argv[1:]
y = 0
for x in data:
	data[y] = x[::-1].swapcase()
	y = y + 1
print(' '.join(reversed(data)))
