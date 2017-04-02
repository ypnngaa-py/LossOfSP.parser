import sys
dic={}
for l in open('SignalPepInfo.csv'):
    ls=l.strip().split('\t')
    dic[ls[0]]=ls[1]+'\t'+ls[2]+'\t'+ls[3]+'\t'+ls[4]+'\t'+ls[5]
#f=open('Extended_Mut_on_Sig.csv','w')

f1=open('Extended_Mut_on_Sig_Germline_total.csv','w')
for r in open('../../../MutationDensity_Project/Dataset_Mutation/sub_Uni_SNPdb_ns_s3.tsv'):
    rs=r.strip().split('\t')
    if rs[1] in dic:
        #if int(rs[2])<=int(dic[rs[1]].split('\t')[4]):
        if int(rs[2])<=70 and int(rs[2])>int(dic[rs[1]].split('\t')[4]):
            f1.write('\t'.join(rs+dic[rs[1]].split('\t'))+'\n')

    
f2=open('Extended_Mut_on_Sig_Somatic_total.csv','w')
for r in open('../../../MutationDensity_Project/Dataset_Mutation/sub_Uni_BioMuta3_ns_s3.tsv'):
    rs=r.strip().split('\t')
    if rs[1] in dic:
        #if int(rs[2])<=int(dic[rs[1]].split('\t')[4]):
        if int(rs[2])<=70 and int(rs[2])>int(dic[rs[1]].split('\t')[4]):
            f2.write('\t'.join(rs+dic[rs[1]].split('\t'))+'\n')