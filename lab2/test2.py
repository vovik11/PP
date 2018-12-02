import xml.etree.ElementTree as ET

root = ET.Element("data")
child = ET.SubElement(root, "text")
tree = ET.ElementTree(root)
tmp = {}
with open('a.txt', encoding='utf-8') as f:
    for i in f.read().split():
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
f.close()
for word, times in tmp.items():
    ET.SubElement(child, "Word", word=word).text = str(times) + " times"
tree.write("list.xml", encoding='utf-8')
