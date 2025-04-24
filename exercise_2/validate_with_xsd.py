from lxml import etree

from pathlib import Path

data_dir = Path.cwd() / "data"

# Load XSD
with open(data_dir / "book.xsd") as xsd_file:
    schema_doc = etree.parse(xsd_file)
    schema = etree.XMLSchema(schema_doc)

# Load XML
xml_doc = etree.parse(data_dir / "book.xml")

# Validate
if schema.validate(xml_doc):
    print("XML is valid according to XSD.")
else:
    print("XML is invalid:")
    for error in schema.error_log:
        print(error.message)