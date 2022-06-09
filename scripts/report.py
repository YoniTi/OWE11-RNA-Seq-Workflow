input = snakemake.input
output = snakemake.output

counter = 0
counter2 = 0
geneIDList = []
convertedGeneIDList = []
seqList = []
functionList = []
pubMedIDList = []
pathwayList = []
sortedPubMedIDList = []
countPubMedIDList = []
		
with open(input[0], "r") as f1, open(input[1], "r") as f2, open(input[2], "r") as f3, open(input[3], "r") as f4, open(input[4], "r") as f5, open(input [5], "r") as f6, open(input[6], "r") as f7, open(output[0], 'w') as outfile:
	outfile.write("Results of the workflow"+'\n'+'\n')
			
	outfile.write("Genes in order of quantity of PubMed articles sorted by low to high:"+'\n')
	for line in f7:
		if "Gene:" in line:
			countPubMedIDList = []
			lineList = line.split('\n')
			sortedPubMedID = lineList[0]
			sortedPubMedIDList.append(sortedPubMedID)
			outfile.write(sortedPubMedIDList[counter2]+'\n')
			counter2+=1
			
	outfile.write('\n'+"Results by Gene:"+'\n'+'\n')
	for line in f1:
		lineList = line.split('\n')
		geneID = lineList[0]
		geneIDList.append(geneID)
	for line in f2:
		lineList = line.split('\n')
		convertedGeneID = lineList[0]
		convertedGeneIDList.append(convertedGeneID)
	content = f3.read()
	seqList = content.split(">")
	while "" in seqList:
		seqList.remove("")
	for line in f4:
		lineList = line.split('\n')
		function = lineList[0]
		functionList.append(function)
	for line in f5:
		lineList = line.split('\n')
		pubMedID = lineList[0]
		pubMedIDList.append(pubMedID)
	for line in f6:
		lineList = line.split('\n')
		pathway = lineList[0]
		pathwayList.append(pathway)
				
		outfile.write("Gene ID:"+'\t'+geneIDList[counter]+'\n'+"Converted Gene ID:"+'\t'+convertedGeneIDList[counter]+'\n'+"Sequence:"+'\t'+seqList[counter][:-6]+'\n'+"Function:"+'\t'+functionList[counter]+'\n'+"PubMed entries:"+'\t'+pubMedIDList[counter]+'\n'+"KEGG Pathways:"+'\t'+pathwayList[counter]+'\n'+'\n')
		counter+=1
