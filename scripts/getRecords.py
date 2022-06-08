from Bio import Entrez
input = snakemake.input
output = snakemake.output
		
Entrez.email = 'yourmail@gmail.com'
recordList = []
IDList = []
counter = 0
		
with open(input[0], "r") as fasta, open(input[1], "r") as f, open(output[0], 'w') as outfile:
	for line in f:
		lineList = line.split('\n')
		ID = lineList[0]
		IDList.append(ID)
	for line in fasta:
		if ">" in line:
			if "=" in line:
				lineList = line.split("=")
				ID = lineList[1]
				handle = Entrez.esearch(db="pubmed", term=ID, rettype="uilist", retmode="text")
				record = handle.read()
				handle.close()
			else:
				record = ""
			recordList.append(record)
					
	for i in IDList:
		outfile.write("Gene: "+IDList[counter]+'\n'+recordList[counter]+'\n'+"-")
		counter+=1
