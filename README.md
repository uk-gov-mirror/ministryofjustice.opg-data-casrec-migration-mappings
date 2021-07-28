# opg-data-casrec-migration-mappings
Mappings automation and versioning for CasRec migration: Managed by opg-org-infra &amp; Terraform

## Making changes to the mapping spreadsheet

1. Branch off the `opg-data-casrec-migration-mappings` main branch
2. Make your changes in the spreadsheet in `opg-data-casrec-migration-mappings/mapping_spreadsheet/Casrec_Mapping_Document.xlsx` and save in the same location
3. In the terminal, `cd` into the `opg-data-casrec-migration-mappings` folder
4. Make sure docker is running!
5. The run this: `docker-compose run --rm  generate python3 app/app.py` to generate the json defs in the folder `opg-data-casrec-migration-mappings/mapping_definitions`
6. Commit all the json and spreadsheet changes to your branch and PR

## Self versioning

When we commit the mapping spreadsheet and push to a branch with a PR, the following steps are performed via circleci:

- Pull in latest zip from merged folder in s3
- Extract to mapping_definitions_previous
- Generate new mappings json files from current spreadsheet
- Compare the previous merged json files to the current ones and create a diff file
- Zip up the new files
- Upload to s3 bucket with current commit ref
- Print the bucket version to the ci job

These same steps are performed on merge to main.

We can then pull in the latest version from merged or any version we like by specifying the version from our main
casrec migrations repo. There is a helper script in opg-data-casrec-migration to assist with this.

