annotation = input("Introduce your gbk annotation file (.gb): ")

file = open(annotation, mode="r")

conting = {}
seq_start = {}
seq_end = {}
seq_strand = {}

for line in file:
    #line = line.strip()
    #print(line)
    locus = line[0:5]
    #print(acc)
    if locus == "LOCUS":
        cntg = line[0:]
        cntg = cntg.strip()
        cntg = cntg.split()[1]
        print("locus")
        print(cntg)
    elif line[22:32] == "protein_id":
        id = line[34:49]
        conting[id] = ""
        conting[id] = cntg
#print(conting)

file = open(annotation, mode="r")
for line in file:
    line = line.strip()
    #print(line)
    if line[0:4] == "gene":
        var = line [16:]
        #print(var)
    elif line [1:11]=="protein_id":
        #print("ok")
        id= line [13:28]
        seq_start[id]=""
        seq_start[id]=var
        #print(id)
#print(seq_start)

seq_strand = {}
for (key, value) in seq_start.items():
    #print(value[0:10])
    if value[0:10] == "complement":
        keys= str(key)
        #print(keys)
        seq_strand[keys] = ""
        seq_strand[keys] = "negative"
        position_neg = value.replace('(', ' ').replace('..', ' ').replace(')', ' ').split()[2]
        end_neg = value.replace('(', ' ').replace('..', ' ').replace(')', ' ').split()[1]
        print(position_neg)
        seq_start[keys] = ""
        seq_start[keys] = position_neg
        seq_end[keys] = ""
        seq_end[keys] = end_neg
    else:
        keys = str(key)
        #print("other value:", keys)
        seq_strand[keys] = ""
        seq_strand[keys] = "positive"
        position_pos = value.replace('(', ' ').replace('..', ' ').replace(')', ' ').split()[0]
        end_pos = value.replace('(', ' ').replace('..', ' ').replace(')', ' ').split()[1]
        seq_start[keys] = ""
        seq_start[keys] = position_pos
        seq_end[keys] = ""
        seq_end[keys] = end_pos
        print(position_pos)

#print(seq_strand)
#print(seq_start)
#print(conting)

Seq = input("Introduce your contig file (.fasta): ")

file =open (Seq, mode = "r")

seq_dic = {}

line_tem = ""

for line in file:
    line=line.strip()
    if line[0]== ">":
        line_tem=line[1:]
        seq_dic[line_tem]= ""
    else:
        seq_dic[line_tem]+= line
#print(seq_dic)

count_txt=input("introduce your ID file (.txt): ")

list_open = open(count_txt, mode ="r")

list_txt=[]
for x in list_open:
    x = str(x.strip())
    list_txt.append(x)
print(list_txt)

int_seq = list_txt

base_length = input("introduce the length of base pair : ")
bp = base_length

pos_strand = {}
neg_strand = {}

for x in int_seq:
    #print(seq_contg[x])
    for (key,value) in conting.items():
        if key == x:
            start=seq_start[x]
            #print(start)
            con_ting=conting[x]
            sequence=seq_dic[con_ting]
            strand=seq_strand[x]
            if strand == 'positive':
                position=int(start)-int(bp)
                pickseq = sequence[position:int(start)]
                pos_strand[x] = ""
                pos_strand[x]=pickseq
            else:
                position=int(start)+int(bp)
                pickseq = sequence[int(start):position]
                neg_strand[x] = ""
                neg_strand[x] = pickseq

#Export
outname=input ("write out fasta file for positive orientation: ")
fasta=open(outname, 'w')
for(key,value) in pos_strand.items():
    fasta.write(">"+str(key)+ '\n'+str(value)+'\n')
fasta.close()

outname=input ("write out fasta file for negative orientation: ")
fasta=open(outname, 'w')
for(key,value) in neg_strand.items():
    fasta.write(">"+str(key)+ '\n'+str(value)+'\n')
fasta.close()


outname=input ("write out filename: ")
file=open(outname, 'w')
file.write("ID" + " "  "conting" + " " + "start" + " " + "end" + " " + "orientation" + '\n')
for x in int_seq:
    for (key,value) in conting.items():
        if key == x:
            y = conting[x] #conting[key]
            start = seq_start[x]
            end = seq_end[x]
            dir = seq_strand[x]
            file.write(x + " " + y + " " + start + " " + end + " " + dir + '\n')
file.close()




