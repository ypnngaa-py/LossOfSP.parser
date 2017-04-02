import sys,csv,Bio.SeqIO
fout=open('uniprot2015_var.bed','w')
rows=Bio.SeqIO.parse(open(sys.argv[1]),'swiss')
uni_var={}
for r in rows:
	for p in r.features:
		if p.type=='VARIANT':
			if len(list(p.location))==1:
				var_pos=list(p.location)[0]+1
				var_mut=p.qualifiers['description']
				literature='NA'
				if p.qualifiers['description'].find('0000269')!=-1:
					literature='Yes'
				fout.write('{}\t{}\t{}\t{}\n'.format(r.id,var_pos,var_mut,literature))		