from itertools import islice
input = snakemake.input
output = snakemake.output
		
with open(input[0], "r") as f, open(output[0], 'w') as outfile:
		for line in islice(f, 2, None):
			lineList = line.split()
			ID = lineList[0]
			outfile.write(ID+'\n')
