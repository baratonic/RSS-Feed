import xmltodict
import json

def convert_xml_to_json(xml_file, json_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        xml_content = file.read()
    data_dict = xmltodict.parse(xml_content)
    json_data = json.dumps(data_dict, indent=4)
    with open(json_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    convert_xml_to_json('rss_feed.xml', 'rss_feed.json')
