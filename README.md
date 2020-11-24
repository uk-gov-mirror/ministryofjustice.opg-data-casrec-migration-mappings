# opg-data-casrec-migration-mappings
Mappings automation and versioning for CasRec migration: Managed by opg-org-infra &amp; Terraform

## Self versioning

When we commit the mapping spreadsheet and push to a branch the following steps are performed via circleci:

- Pull in latest zip from merged folder in s3
- Extract to mapping_definitions_previous
- Generate new mappings json files from current spreadsheet
- Compare the previous merged json files to the current ones and create a diff file
- Zip up the new files
- Upload to s3 bucket with current commit ref
- Print the bucket version to the ci job

When we merge to main the following steps are performed:

- Copy from the commit version of the stage bucket into the merge bucket overwriting the existing zip file
(and creating a new version)
- Print the latest version to the ci job

We can then pull in the latest version from merged or any version we like by specifying the version from our main
casrec migrations repo. There is a helper script in opg-data-casrec-migration to assist with this.
