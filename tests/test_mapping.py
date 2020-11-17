import json

from docs.support_scripts.mapping_doc_to_json.mapping_all_sheets import Mapping

mapping_doc = "./test_data/test_mapping_doc.xlsx"
output_dir = "./json_output"


def test_mapping_old_format():
    expected_result = "./test_data/rainbows_mapping.json"
    mapping = Mapping(excel_doc=mapping_doc, output_folder=output_dir, new_format=False)
    mapping.generate_json_files()

    with open(expected_result, "r") as expected_json:
        expected_data = expected_json.read()
        expected_dict = json.loads(expected_data)

    with open(f"{output_dir}/rainbows_mapping.json", "r") as result_json:
        result_data = result_json.read()
        result_dict = json.loads(result_data)

    assert sorted(expected_dict) == sorted(result_dict)


def test_mapping_new_format():
    expected_result = "./test_data/rainbows_mapping_new_format.json"
    mapping = Mapping(excel_doc=mapping_doc, output_folder=output_dir, new_format=True)
    mapping.generate_json_files()

    with open(expected_result, "r") as expected_json:
        expected_data = expected_json.read()
        expected_dict = json.loads(expected_data)

    with open(f"{output_dir}/rainbows_mapping.json", "r") as result_json:
        result_data = result_json.read()
        result_dict = json.loads(result_data)

    assert sorted(expected_dict) == sorted(result_dict)
