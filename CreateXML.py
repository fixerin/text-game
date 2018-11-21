import xml.etree.cElementTree as ET

root = ET.Element("lista_pokoi")
doc = ET.SubElement(root, "pokoj")


for i in range(81):
    ET.SubElement(doc, "field1", name="blah").text = "some value1"
    pass


ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"

tree = ET.ElementTree(root)
tree.write("filename.xml")