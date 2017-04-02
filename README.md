# LossOfSP.parser
Customized scripts parsing SignalP 4.1 results to find loss of signal peptide events caused by mutations

Note:
Scripts are highly customized, thus, I do not encourage for generic use. However, they are good for tracking the pipeline details and ensuring the reproducibility.


Main Scripts Usage:
1. Selecting Mutation falling into regions could affect SP (70 aa of proteins with annotated SP in UniProtKB):
SignalRegionMut.py

2. From mutation list to generate mutated protein sequences:
generateMutSeq.py

3. Parse SignalP 4.1 results of reference vs. muatated protein sequences:
getChangeofSP.py
