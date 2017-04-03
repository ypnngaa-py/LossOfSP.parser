# LossOfSP.parser
Customized scripts parsing SignalP 4.1 results to find loss of signal peptide events caused by mutations

## Note:
1. Scripts are highly customized, thus, I do not encourage for generic use. However, they are good for tracking the pipeline details and ensuring the reproducibility.
2. SignalP 4.1 command line can be downlaoded from their website. Default parameters are used for this analysis. Output format (-f) need to be set as short_out to use this paser. Note that sometimes the prediction result file may not formated in python recognizable tab-delimited way. User may need ot format it first


## Main Scripts Usage:
1. Selecting Mutation falling into regions could affect SP (70 aa of proteins with annotated SP in UniProtKB):
```
python SignalRegionMut.py
#Generate FILE_NAME.csv. 
#Uses a compiled mutation datasets based on BioMuta and dbSNP as input. Due to the file size please contact panyang1989@gwu.edu for accessing the file. Description of that file can be found in the paper.  
```
2. From mutation list to generate mutated protein sequences:
```
python generateMutSeq.py FILE_NAME.csv
#Generate mutseq.FILE_NAME.csv.fasta, which can be used as SignalP 4.1 input file.
```
3. Parse SignalP 4.1 results of reference vs. muatated protein sequences:
```
python getChangeofSP.py mutseq.FILE_NAME.csv.fasta.short_out FILE_NAME.csv 
#Note that sometimes the prediction result file may not formated in python recognizable tab-delimited way. User may need ot format it first (refers to mutseq.FILE_NAME.csv.fasta.short_out).
```

