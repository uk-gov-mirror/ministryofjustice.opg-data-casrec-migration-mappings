import filecmp

import click as click

from app.helper import assume_aws_session
from app.mapping_all_sheets import Mapping
from app.upload_to_s3 import copy_latest_s3
from app.upload_to_s3 import extract_zip
from app.upload_to_s3 import get_latest_version
from app.upload_to_s3 import pull_latest_merged
from app.upload_to_s3 import report_recursive
from app.upload_to_s3 import upload_file
from app.upload_to_s3 import zip_dir


@click.command()
@click.option("--new_format", default=True)
@click.option("--commit", default=None)
@click.option("--ci_stage", default="pull_request")
@click.option("--role", default="operator")
def main(new_format, commit, ci_stage, role):
    dirs_to_zip = ["mapping_spreadsheet", "mapping_definitions"]

    zip_file_pre = "mappings"
    ext = ".zip"
    zip_file = f"{zip_file_pre}{ext}"
    account = "288342028542"
    s3_folder = "staged"
    previous_folder = "mapping_definitions_previous"
    bucket_name = "casrec-migration-mappings-development"
    s3_file_path = f"{s3_folder}/{zip_file_pre}_{commit}{ext}"
    s3_file_path_merged = f"merged/{zip_file_pre}{ext}"
    s3_session = assume_aws_session(account, role)
    s3 = s3_session.client("s3")
    output_file = "./mapping_definitions/summary/file_diffs.txt"

    if ci_stage == "pull_request":

        pull_latest_merged(bucket_name, s3, zip_file)
        extract_zip(zip_file, previous_folder)

        mapping_doc_name = "Casrec_Mapping_Document.xlsx"

        mapping = Mapping(mapping_doc_name=mapping_doc_name, new_format=new_format,)
        mapping.generate_json_files()

        directory_comparison = filecmp.dircmp(
            "mapping_definitions_previous/mapping_definitions", "mapping_definitions"
        )
        report_recursive(directory_comparison, output_file)

        zip_dir(dirs_to_zip, zip_file)
        upload_file(bucket_name, zip_file, s3, s3_file_path)
        print(get_latest_version(bucket_name, s3_file_path, s3))
    elif ci_stage == "merge_main":
        copy_latest_s3(bucket_name, s3, s3_file_path, s3_file_path_merged, zip_file)
        print(get_latest_version(bucket_name, s3_file_path_merged, s3))
    else:
        print("Unknown stage")


if __name__ == "__main__":

    main()
