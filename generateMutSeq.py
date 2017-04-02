import sys, Bio.SeqIO

def read_ori_seq():
	ori_seq={}
	for record in Bio.SeqIO.parse(open('uniprot2015.fa'),'fasta'):
		ori_seq[record.id]=str(record.seq)
	return ori_seq

def generate_mut_seq(ori_seq,prot_id,prot_pos,prot_aa,mut_aa,seq_len):
	seq=ori_seq[prot_id][0:int(seq_len)]
	if seq[int(prot_pos)-1]==prot_aa:
		mut_seq=seq[0:int(prot_pos)-1]+mut_aa+seq[int(prot_pos):]

	else:
		print 'err',prot_id,prot_pos,prot_aa
		mut_seq=''
	return mut_seq
def main():
	fout=open('mutseq.'+sys.argv[1]+'.fasta','w')
	ori_seq=read_ori_seq()
	for l in open(sys.argv[1]):
		ls=l.strip().split('\t')
		#mut_seq=generate_mut_seq(ori_seq,ls[1],ls[2],ls[3],ls[4],ls[17])
		mut_seq=generate_mut_seq(ori_seq,ls[1],ls[2],ls[3],ls[4],70)
		if mut_seq!='':
			fout.write('>{}\n{}\n'.format(ls[1]+'_'+ls[2]+'_'+ls[4],mut_seq))

if __name__ == '__main__':
	main()