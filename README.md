# config-files-validator
A command line tool to validate configuration language files and template files. So far json, yaml, jinja2, and toml are supported. The tool validates
the files by trying load them one by one. Result can be converted to xunit xml report.

## Example of usage with json files
```
validate-json-files example1.json example2.json
```

## Example of usage with yaml files
```
validate-yaml-files example1.yaml example2.yaml
```

## Example of usage with jinja2 files
```
validate-jinja2-files example1.j2 example2.j2
```

## Example of usage with jinja2 files and extensions
```
validate-jinja2-files --j2-extensions=jinja2.ext.do,jinja2.ext.i18n example1.j2 example2.j2
```

## Example of usage with toml files
```
validate-toml-files example1.toml example2.toml
```

## Example of xunit xml report
This will generate an xunit xml report file named testreport.xml
```
validate-yaml-files example1.yaml example2.yaml --xunit
```
This will generate an xunit xml report file named myxunit.xml
```
validate-yaml-files example1.yaml example2.yaml --xunit --xunit-output-file=myxunit.xml
```

## Requirements
The tool requires version 3.8 or higher of Python.

![ci](https://github.com/feffe/config-files-validator/workflows/CI/badge.svg?branch=master)
