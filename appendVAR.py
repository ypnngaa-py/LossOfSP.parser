import sys
def read_VAR():
	uni_var={'+'.join(l.split('\t')[:2]):l.split('\t')[2] for l in open('uniprot2015_var.bed') if l.strip().split('\t')[-1]=='Yes'}
	return uni_var

uni_var=read_VAR()
fout=open('var.'+sys.argv[1],'w')
for l in open(sys.argv[1]):
	ls=l.strip().split()
	if ls[1]+'+'+ls[2] in uni_var:
		if ls[3]+' -> '+ls[4] in uni_var[ls[1]+'+'+ls[2]]:
			fout.write(l.strip()+'\t'+uni_var[ls[1]+'+'+ls[2]]+'\n')
		else:
			fout.write(l.strip()+'\t[Not Exact] '+uni_var[ls[1]+'+'+ls[2]]+'\n')
	else:
		fout.write(l.strip()+'\tNA\n')

