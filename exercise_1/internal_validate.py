from lxml import etree
from pathlib import Path

data_dir = Path.cwd() / "data"

# Load the XML with internal DTD
with open(data_dir / "internal_dtd_example.xml", "rb") as xml_file:
    parser = etree.XMLParser(dtd_validation=True)
    try:
        etree.parse(xml_file, parser)
        print("XML is valid against the internal DTD.")
    except etree.XMLSyntaxError as e:
        print("XML validation error:")
        print(e)