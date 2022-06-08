from Bio import Entrez
input = snakemake.input
output = snakemake.output
		
Entrez.email = 'yourmail@gmail.com'
		
with open(input[0], "r") as f, open(output[0], 'w') as outfile:
		for line in f:
			lineList = line.split('\n')
			ID = lineList[0]
			handle = Entrez.esearch(db="protein", term=ID)
			record = Entrez.read(handle)
			handle.close()
					
			searchID = (record['IdList'])
			searchID = str(searchID[0])
			outfile.write(searchID+'\n')
