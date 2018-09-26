# config-files-validator
A command line tool to validate configuration language files. So far json and yaml are supported. The tool validates
the files by trying load them one by one. Result can be converted to xunit xml report.

## Example of usage with json files
```
validate-json-files example1.json example2.json
```

## Example of usage with yaml files
```
validate-yaml-files example1.yaml example2.yaml
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
The tool requires version 3.6 or higher of Python.