from lxml import etree
from pathlib import Path

data_dir = Path.cwd() / "data"

# Load the XML file
with open(data_dir / "library.xml", "rb") as xml_file:
    xml_doc = etree.parse(xml_file)

# Load and parse the external DTD
with open(data_dir / "library.dtd", "rb") as dtd_file:
    dtd = etree.DTD(dtd_file)

# Validate the XML file against the DTD
if dtd.validate(xml_doc):
    print("XML is valid according to the DTD.")
else:
    print("XML is not valid.")
    print("Validation errors:")
    print(dtd.error_log.filter_from_errors())