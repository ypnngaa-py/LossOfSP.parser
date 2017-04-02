import sys,csv,Bio.SeqIO
loc={}
gn={}
exp={}
sec={}
f=open('SignalPepInfo.csv','w')
rows=Bio.SeqIO.parse(open(sys.argv[1]),'swiss')
for r in rows:
    try:
        genename=r.annotations['gene_name'].split(';')[0].split('=')[1].strip()
        gn[r.id]='N/A'
        if genename!='':
           gn[r.id]=genename
    except KeyError:
        gn[r.id]='N/A'
    sec[r.id]='Non-secreted'
    for kw in r.annotations['keywords']:
        if kw=='Secreted':
            sec[r.id]='Secreted'            
    for a in r.features:
        if a.type=='SIGNAL':
            loc[r.id]=str(a.location).strip()
            exp[r.id]=a.qualifiers['description'].strip('.').strip()
    pos=70
    if sec[r.id]=='Secreted':
        try:
            pos=int(loc[r.id].strip('[]').split(':')[1])+30
        except ValueError:
            pos=70
    f.write('\t'.join([r.id,gn[r.id],sec[r.id],exp[r.id],loc[r.id],str(pos)])+'\n')
    
    
