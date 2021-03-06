# OWE11 RNA-Seq-Workflow
A workflow for getting information of genes based on RNA-seq data. This workflow is build using Snakemake and uses various scripts to gather all requested information.

## Get started using Linux
### Copy this repo in a new directory
  `> git clone https://github.com/YoniTi/OWE11-RNA-Seq-Workflow.git`

### Remove data files
Because this workflow is tested previously, please remove everything from the `data` directory except `RNA-Seq-counts.txt`. Also remove `report.txt` from the root directory.

### Next install Miniconda 3

  `$ wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh`
    
  `$ bash Miniconda3-latest-Linux-x86_64.sh`

### Create new conda environment with the provided environment file
  Please note: you have to open the `environment.yaml` file and add your own name at `name: `
  
  `$ conda env create --file {path-to-file}/environment.yaml`

  To activate your environment:

  `$ source activate {your-environment-name}`

  To deactivate:

  `$ source deactivate`
  
### Run the workflow by using the `snakemake` command
  
  `$ snakemake {optional parameters}`
  
To run the complete workflow use `$ snakemake report`

Please note: `$ snakemake report` only works if there is no `report.txt` file in the project directory.

To visualize the workflow in a pdf use `$ snakemake visualize`


After running the workflow you can find a `report.txt` file in the root of the project directory.
The report shows all genes in order of quantity of PubMed articles sorted by low to high. To see specific data files see the `data` directory.

## The report contains the following information:
* Gene ID
* Converted Gene ID
* Sequence
* Function
* Pubmed entries
* Pathway


## The workflow is visualized in dag.pdf in the root directory
If this file is missing please run `$ snakemake visualize` in the terminal.

The workflow consists of 9 steps where everything combines in the last step `report`
