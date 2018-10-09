import xml.etree.ElementTree as ET
from xml.dom import minidom

def unlist(numbers, result = []):

    for number in numbers:
        if type(number) == list:
            unlist(number)
        else:
            result.append(number)

    return result

def prettify(elem):

    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

f = open('a.txt', 'r')
word2 = []
for line in f:
    word2.append(line.split(" "))

f.close()

word2 = unlist(word2)
print(word2)

word3 = []

for i,q in enumerate(word2):
    if(word2[i]) == '\n':
        word2.remove('\n')

for t,i in enumerate(word2):
    if i[int(len(i)-2)] == '.':
        print("find")

for i in word2:
    word3.append(i.strip(' ,.\n'))

print(word3)

word4 = []

bool = False
for i in word3:
    for j in word4:
        if str(i) == str(j):
            bool = True
    if bool == False:
        word4.append(i)
    bool = False


data = ET.Element('data')
words = ET.SubElement(data,'words')
item1 = ET.SubElement(words,'item')

item1.set('name','item1')
item1.text = 'item1text'

for i,element in enumerate(word4):
    element = ET.SubElement(words,'word')
    element.set('name',str(word4[i]))
    count = 0
    for k in word3:
        if str(k) == str(word4[i]):
            count+=1
    element.text = ' ' + str(count) + " "


mydata = prettify(data)
#mydata = ET.tostring(data)
#handle = ET.tostring(data)
myfile = open("test2.xml",'w')
myfile.write(str(mydata))

