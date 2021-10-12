import xml.etree.ElementTree as decoder
DataTree = decoder.ElementTree(file="menu.xml")
root = DataTree.getroot()

for child in root:
    print(child.tag)
    Title = list(child.attrib.keys())[0]
    hr = list(child.attrib.values())[0]
    print("%s: %s" %(Title, hr))
    for item in child:
        print("%s, %s: %s" %(item.text, list(item.attrib.keys())[0], list(item.attrib.values())[0]))