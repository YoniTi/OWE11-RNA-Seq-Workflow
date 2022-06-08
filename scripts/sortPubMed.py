input = snakemake.input
output = snakemake.output

counter = 0
		
with open(input[0], "r") as f, open(output[0], 'w') as outfile:
	content = f.read()
	pmList = content.split("-")
	pmList.sort(key = len, reverse=True)
			
	for i in pmList:
				
		outfile.write(pmList[counter])
		counter+=1
