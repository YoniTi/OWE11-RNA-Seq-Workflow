from Bio import Entrez
import re
input = snakemake.input
output = snakemake.output
		
Entrez.email = 'yourmail@gmail.com'
		
with open(input[0], "r") as f, open(output[0], 'w') as outfile:
	for line in f:
		lineList = line.split('\n')
		ID = lineList[0]
		handle = Entrez.efetch(db="protein", id=ID, rettype="ft", retmode="text")
		record = handle.read()
		handle.close()
				
		function = re.search('note.*',record).group(0)
		function = function.strip('note\t')
		outfile.write(str(function)+'\n')
