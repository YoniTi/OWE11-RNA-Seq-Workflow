from bioservices import KEGG
input = snakemake.input
output = snakemake.output
		
s = KEGG()
IDList = []
counter = 0
		
with open(input[0], "r") as f, open(output[0], 'w') as outfile:
	for line in f:
		lineList = line.split('\n')
		ID = lineList[0]
				
		IDList.append(ID)
		pathway = s.get_pathway_by_gene(ID,"lpl")
		if pathway == None:
			pathway = ""
		outfile.write(IDList[counter]+'\t'+str(pathway)+'\n')
		counter+=1
