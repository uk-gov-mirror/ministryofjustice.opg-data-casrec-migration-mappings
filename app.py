import click as click

from app.helper import assume_aws_session
from app.mapping_all_sheets import Mapping
from app.upload_to_s3 import copy_latest_s3
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
    bucket_name = "casrec-migration-mappings-development"
    s3_file_path = f"{s3_folder}/{zip_file_pre}_{commit}{ext}"
    s3_file_path_merged = f"merged/{zip_file_pre}{ext}"
    s3_session = assume_aws_session(account, role)
    s3 = s3_session.client("s3")

    if ci_stage == "pull_request":

        mapping_doc_name = "Casrec_Mapping_Document.xlsx"

        mapping = Mapping(mapping_doc_name=mapping_doc_name, new_format=new_format,)
        mapping.generate_json_files()

        zip_dir(dirs_to_zip, zip_file)

        upload_file(bucket_name, zip_file, s3, s3_file_path)

    elif ci_stage == "merge_main":
        copy_latest_s3(bucket_name, s3, s3_file_path, s3_file_path_merged, zip_file)
    else:
        print("Unknown stage")


if __name__ == "__main__":

    main()
