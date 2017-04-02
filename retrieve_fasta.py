import sys,csv,Bio.SeqIO
fout=open('uniprot2015.fa','w')
rows=Bio.SeqIO.parse(open(sys.argv[1]),'swiss')
for r in rows:
	fout.write('>{}\n{}\n'.format(r.id,str(r.seq)))