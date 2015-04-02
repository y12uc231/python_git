#Satyapriya krishna
#Print the email id who has sent the highest email id from a file mbox-short.txt
name = raw_input("Enter file:")
dic=dict()
lis=list()
file=open(name,'r')
for line in file:
	if line.startswith('From'):
	  lis=line.split()
	  dic[lis[1]]=dic.get(lis[1],0)+1
        
ma=0

for key in dic:
	if (dic[key]>ma):
        ma=dic[key]
        val=key

print val,"	",ma      