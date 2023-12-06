with open('Parsing exercise/headers.txt') as f:
    headers=f.readlines()

print(headers[:2])

stripped_headers=[]

for line in headers:
    stripped_headers.append(line[8:-2]) #string indexing

print(stripped_headers[0:2])
#string.split function
#each string is now a list, then u can just iterate through the list and extract each value by using indexing again

split_headers=[]
for line in stripped_headers:
    split_headers.append(line.split(','))

print(split_headers[:2])

#print(type(headers))
#print(headers)

#headers_2=[]

#for header in headers:
#    headers_2.append(header.removeprefix('##INFO=<').removesuffix('>\n').split(","))

#print(headers_2[:2])

#header_1=[entry.split('=') for entry in headers_2[0]]
#print(header_1)

#dictionary_1={}
#dictionary_1[header_1[0][0]]=header_1[0][1]

#for entry in header_1:
#    for x,y in entry:
#        dictionary_1[x]=y
#        print(x)
#        print(y)


#    dictionary_1[entry[0]]=entry[1]

#print(dictionary_1)