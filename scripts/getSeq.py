from Bio import Entrez
input = snakemake.input
output = snakemake.output
		
Entrez.email = 'yourmail@gmail.com'
		
with open(input[0], "r") as f, open(output[0], 'w') as outfile:
	for line in f:
		lineList = line.split('\n')
		ID = lineList[0]
		handle = Entrez.efetch(db="protein", id=ID, rettype="fasta", retmode="text")
		record = handle.read()
		handle.close()
				
		outfile.write(record+'\n')
