#
#	Process the logger, get the average amounts of each object.
#
lines = open("log.txt").readlines()
lines = [l.strip() for l in lines if l[:4] == "Coal"]

totals = {}
lineCount = 0
for l in lines:
	lineCount = lineCount + 1
	for item in l.split(" "):
		name = item.split("=")[0]
		count = int(item.split("=")[1])
		if name not in totals:
			totals[name] = 0
		totals[name] = totals[name] + count

for k in totals.keys():
	print(k,totals[k]/lineCount)