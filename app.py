import click as click

from app.mapping_all_sheets import Mapping


@click.command()
@click.option(
    "--new_format", prompt=f"use new format?", default=True,
)
def main(new_format):

    mapping_doc_name = "Casrec_Mapping_Document_v0.1.xlsx"

    mapping = Mapping(mapping_doc_name=mapping_doc_name, new_format=new_format,)
    mapping.generate_json_files()


if __name__ == "__main__":

    main()
