import os


dirname = os.path.dirname(__file__)
test_file_paths = {
    "mapping_spreadsheet": os.path.join(dirname, "./test_data"),
    "json_template": "./app/template",
    "mapping_definitions_output": os.path.join(dirname, "./json_output"),
    "lookup_tables_output": os.path.join(dirname, "./json_output/lookups"),
    "summary_output": os.path.join(dirname, "./docs"),
}
mapping_doc = "test_mapping_doc.xlsx"
expected_options = os.path.join(dirname, "./test_data/options.json")
