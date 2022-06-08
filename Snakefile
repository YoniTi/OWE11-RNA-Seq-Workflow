# Titel: OWE11 RNA-Seq-Workflow
# Author: Yoni Tielemans
# Version: 1.0
# Date: 08-06-2022

# Snakemake rules
# Read a RNA Seq counts file with gene IDs
rule preprocessing:
	input:
		"data/RNA-Seq-counts.txt"
	output:
		"data/geneIDs.txt"
	script:
		"scripts/preprocessing.py"	

# Recognize gene ID type and convert to numerical gene identifier
rule convertGeneIDs:
	input:
		"data/geneIDs.txt"
	output:
		"data/convertedGeneIDs.txt"
	script:
		"scripts/convertGeneIDs.py"

# Get the sequence of the gene
rule getSeq:
	input:
		"data/convertedGeneIDs.txt"
	output:
		"data/seqs.fasta"
	script:
		"scripts/getSeq.py"

# Get the function of the gene
rule getFunction:
	input:
		"data/convertedGeneIDs.txt"
	output:
		"data/functions.txt"
	script:
		"scripts/getFunction.py"

# Get PubMed IDs of the genes
rule getRecords:
	input:
		"data/seqs.fasta",
		"data/convertedGeneIDs.txt"
	output:
		"data/records.txt"
	script:
		"scripts/getRecords.py"

# Get PubMed IDs for all genes
rule getPubMed:
	input:
		"data/records.txt"
	output:
		"data/pubMedIDs.txt"
	script:
		"scripts/getPubMed.py"

# Sort genes based on PubMed IDs
rule sortPubMed:
	input:
		"data/pubMedIDs.txt"
	output:
		"data/sortedPubMedIDs.txt"
	script:
		"scripts/sortPubMed.py"

# Get KEGG pathways of the genes (shown as KEGG IDs)
rule getPathway:
	input:
		"data/geneIDs.txt"
	output:
		"data/pathways.txt"
	script:
		"scripts/getPathway.py"

# Combine all gene information in a report
rule report:
	input:
		"data/geneIDs.txt",
		"data/convertedGeneIDs.txt",
		"data/seqs.fasta",
		"data/functions.txt",
		"data/pubMedIDs.txt",
		"data/pathways.txt",
		"data/sortedPubMedIDs.txt"
	output:
		"report.txt"
	script:
		"scripts/report.py"

# Visualize snakemake workflow with --dag
rule visualize:
	output:
		"dag.pdf"
	shell:
		"snakemake --dag report | dot -Tpdf > dag.pdf"
