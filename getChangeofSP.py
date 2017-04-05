import sys

def read_pred(fin, comma):
	pred_dict={}
	for l in open(fin):
		if l.startswith('#'):
			continue
		ls=l.strip().split('\t')
		if comma:
			ls=l.strip().split(',')
		pred_dict[ls[0].strip()]=ls[9]+'+'+ls[4]+'+'+ls[10]+'+'+ls[8]

	return pred_dict


ori_pred_dict=read_pred('uniprot2015.short_out',False)
mut_pred_dict=read_pred(sys.argv[1],True)
fout=open('sum.change.'+sys.argv[1],'w')
for l in open(sys.argv[2]):
	ls=l.strip().split('\t')
	[ori_pred_has,ori_pred_pos,ori_cutoff,ori_dscore]=ori_pred_dict[ls[1]].split('+')
	[mut_pred_has,mut_pred_pos,mut_cutoff,mut_dscore]=mut_pred_dict[ls[1]+'_'+ls[2]+'_'+ls[4]].split('+')
	correct='Correct'
	effect='Unchanged'
	if int(ori_pred_pos)!=int(mut_pred_pos):
		effect='Cleavage_change'
	if ori_pred_has=='Y' and mut_pred_has=='N':
		effect='Loss_SP'
	delta_dscore=str(float(mut_dscore)-float(ori_dscore))
	try:
		if int(ori_pred_pos)-1!=int(ls[-2].split(':')[1][:-1]):
			correct='Inconsistent_in_pos'
		if ori_pred_has!='Y':
			correct='Inconsistent'
		fout.write(l.strip()+'\t'+effect+'\t'+correct+'\t'+mut_pred_has+'\t'+mut_cutoff+'\t'+mut_dscore+'\t'+delta_dscore+'\t'+mut_pred_pos+'\n')
	except ValueError:
		correct='Unknown'
		effect='Unknown'
		fout.write(l.strip()+'\t'+effect+'\t'+correct+'\t'+mut_pred_has+'\t'+mut_cutoff+'\t'+mut_dscore+'\t'+delta_dscore+'\t'+mut_pred_pos+'\n')
