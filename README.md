# opg-data-casrec-migration-mappings
Mappings automation and versioning for CasRec migration: Managed by opg-org-infra &amp; Terraform

## To run and generate the mapping files

1. Create a venv
2. `pip3 install -r requirements`
3. `python3 app.py`
4. You will then be asked if you want the files in the new format (default True)
5. Json files will appear in the `mapping_definitions` folder


### But this is not very good is it...

No, but we will shortly be adding some more fancy stuff so that the files are generated automatically and uploaded to s3. Then in the [migrations project](https://github.com/ministryofjustice/opg-data-casrec-migration) we will pull the files directly from s3.

But that is a future problem, for now you will just have to copy the files to where you need them.
