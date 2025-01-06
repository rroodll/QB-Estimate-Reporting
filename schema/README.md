# Resource Estimate JSON Schema


The `resource_estimate_schema.json` can be used to validate that a submitted resource estimate JSON file is valid (i.e., contains all required fields with appropriately typed values.)

Validation can be performed in several ways including:

1. By including the `$schema` field *directly* inside of all submitted resource estimate files, Microsoft VS code (and possibly other editors) are smart enough to fetch the schema from the URL and lint the file.  Microsoft VS code may be manually configured to associate a schema with a file as well.
2. Using the Python package `jsonschema`
    - directly from the command line as `jsonschema -i my_re.json resource_estimate_schema.json` (referencing the local `resource_estimate_schema.json` file) or
    - within a customized Python script such as `validate_json_file.py` which will perform an HTTP request to fetch the latest schema.  See `validate_json_file.py --help` for usage.
3. Using any one of the myriad of other JSON validation tools.










