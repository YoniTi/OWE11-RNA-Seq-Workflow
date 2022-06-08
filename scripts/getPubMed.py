input = snakemake.input
output = snakemake.output

with open(input[0], "r") as f, open(output[0], 'w') as outfile:
	for line in f:
		lineList = line.split('\n')
		if "<" in line:
			if "<Id>" in line:
				line = line.strip("<Id>")
				line = line[:-6]
				outfile.write(line+'\n')
		else:
			outfile.write(line)
