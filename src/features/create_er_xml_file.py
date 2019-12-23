import json
import xmltodict
from src.features.find_cardinality import relation
import glob
from xml.etree import ElementTree


table = []
folder = "src\\data"


def run(folder):
    files = glob.glob(folder + "/*.xml")
    first = None

    for filename in files:
        data = ElementTree.parse(filename).getroot()
        if first is None:
            first = data
        else:
            first.extend(data)
    if first is not None:
        config = ElementTree.tostring(first).decode()
        with open("src\\data\\first_output.xml", "w+", encoding="utf-8") as h:
            h.write(config)


def create_output_xml_file():
    # print(relation)

    output_dic = {'er': {'relation': relation}}

    with open('src\\data\\relation.json', 'w+') as json_file:
        json.dump(output_dic, json_file, indent=4, sort_keys=True)

    output_xml = xmltodict.unparse(output_dic, pretty=True)

    with open('src\\data\\relation.xml', 'w+') as xml_file:
        xml_file.write(output_xml)

    run(folder)
