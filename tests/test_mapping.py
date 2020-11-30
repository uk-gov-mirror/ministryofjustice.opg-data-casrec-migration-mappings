import json

from app.mapping_all_sheets import Mapping
from tests.conftest import expected_options
from tests.conftest import mapping_doc
from tests.conftest import test_file_paths


def test_mapping_old_format():
    expected_result = f"{test_file_paths['mapping_spreadsheet']}/rainbows_mapping.json"
    mapping = Mapping(
        mapping_doc_name=mapping_doc, new_format=False, file_paths=test_file_paths
    )
    mapping.generate_json_files()

    with open(expected_result, "r") as expected_json:
        expected_data = expected_json.read()
        expected_dict = json.loads(expected_data)

    with open(
        f"{test_file_paths['mapping_definitions_output']}/rainbows_mapping.json", "r"
    ) as result_json:
        result_data = result_json.read()
        result_dict = json.loads(result_data)

    assert sorted(expected_dict) == sorted(result_dict)


def test_mapping_new_format():
    expected_result = (
        f"{test_file_paths['mapping_spreadsheet']}/rainbows_mapping_new_format.json"
    )
    mapping = Mapping(
        mapping_doc_name=mapping_doc, new_format=True, file_paths=test_file_paths
    )
    mapping.generate_json_files()

    with open(expected_result, "r") as expected_json:
        expected_data = expected_json.read()
        expected_dict = json.loads(expected_data)

    with open(
        f"{test_file_paths['mapping_definitions_output']}/rainbows_mapping.json", "r"
    ) as result_json:
        result_data = result_json.read()
        result_dict = json.loads(result_data)

    assert sorted(expected_dict) == sorted(result_dict)

    # check all transform_casrec details
    for colour, details in expected_dict.items():
        assert (
            result_dict[colour]["transform_casrec"]["casrec_table"]
            == details["transform_casrec"]["casrec_table"]
        )
        assert (
            result_dict[colour]["transform_casrec"]["casrec_column_name"]
            == details["transform_casrec"]["casrec_column_name"]
        )
        assert (
            result_dict[colour]["transform_casrec"]["alias"]
            == details["transform_casrec"]["alias"]
        )
        assert (
            result_dict[colour]["transform_casrec"]["requires_transformation"]
            == details["transform_casrec"]["requires_transformation"]
        )
        assert (
            result_dict[colour]["transform_casrec"]["lookup_table"]
            == details["transform_casrec"]["lookup_table"]
        )
        assert (
            result_dict[colour]["transform_casrec"]["default_value"]
            == details["transform_casrec"]["default_value"]
        )
        assert (
            result_dict[colour]["transform_casrec"]["calculated"]
            == details["transform_casrec"]["calculated"]
        )
