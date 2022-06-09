input = snakemake.input
output = snakemake.output
		
with open(input[0], "r") as f, open(output[0], 'w') as outfile:
    for line in f:
        if line.startswith("#") or line.startswith("ID"):
            next(f)
        else:
            if line.strip() !="":
            	outfile.write((line.split("\t")[0]+"\n"))

