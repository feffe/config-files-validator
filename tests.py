from io import StringIO

import pytest

from config_files.validator import (
    Result,
    xunit_report,
    json_validation_result,
    yaml_validation_result,
    jinja2_validation_result,
    toml_validation_result,
)


def unprettyfy_xml(xml):
    return xml.replace("\t", "").replace("\n", "")


@pytest.fixture
def passed_result():
    return Result(passed=True, path="path/to/passed/test")


@pytest.fixture
def failed_result():
    return Result(passed=False, path="path/to/failed/test", msg="error message")


def test_result_output_for_passed_test(passed_result):
    assert passed_result.to_output() == "path/to/passed/test PASSED"


def test_result_output_for_failed_test(failed_result):
    assert failed_result.to_output() == "path/to/failed/test FAILED\nerror message"


def test_xunit_report_with_no_tests():
    expected_report = '<?xml version="1.0" ?><testsuites disabled="0" errors="0" failures="0" tests="0" time="0.0"><testsuite disabled="0" errors="0" failures="0" name="yaml" skipped="0" tests="0" time="0"/></testsuites>'
    assert unprettyfy_xml(xunit_report(results=[], file_type="yaml")) == expected_report


def test_xunit_report_with_no_failing_tests(passed_result):
    expected_report = '<?xml version="1.0" ?><testsuites disabled="0" errors="0" failures="0" tests="1" time="0.0"><testsuite disabled="0" errors="0" failures="0" name="yaml" skipped="0" tests="1" time="0"><testcase name="path/to/passed/test"/></testsuite></testsuites>'
    assert unprettyfy_xml(xunit_report(results=[passed_result], file_type="yaml")) == expected_report


def test_xunit_report_with_failing_test(passed_result, failed_result):
    expected_report = '<?xml version="1.0" ?><testsuites disabled="0" errors="0" failures="1" tests="2" time="0.0"><testsuite disabled="0" errors="0" failures="1" name="yaml" skipped="0" tests="2" time="0"><testcase name="path/to/passed/test"/><testcase name="path/to/failed/test"><failure type="failure" message="error message"/></testcase></testsuite></testsuites>'
    assert unprettyfy_xml(xunit_report(results=[passed_result, failed_result], file_type="yaml")) == expected_report


def test_valid_json():
    json = StringIO('{"a": "b"}')
    json.name = "path/to/file"
    assert json_validation_result(json).passed


def test_invalid_json():
    json = StringIO('invalid{"a": "b"}')
    json.name = "path/to/file"
    assert not json_validation_result(json).passed


def test_valid_yaml():
    yaml = StringIO("a: b")
    yaml.name = "path/to/file"
    assert yaml_validation_result(yaml).passed


def test_valid_multi_document_yaml():
    yaml = StringIO("---\na: b\n---\nc: d")
    yaml.name = "path/to/file"
    assert yaml_validation_result(yaml).passed


def test_invalid_yaml():
    yaml = StringIO("a: b, c: d")
    yaml.name = "path/to/file"
    assert not yaml_validation_result(yaml).passed


def test_valid_jinja2():
    j2 = StringIO("{% for a in b %}{% endfor %}")
    j2.name = "path/to/file"
    assert jinja2_validation_result(j2).passed


def test_invalid_jinja2():
    j2 = StringIO("{% for a in b %}")
    j2.name = "path/to/file"
    assert not jinja2_validation_result(j2).passed


def test_valid_jinja2_with_extension():
    j2 = StringIO("{% do navigation.append('a string') %}")
    j2.name = "path/to/file"
    assert jinja2_validation_result(j2, extensions=["jinja2.ext.do"]).passed


def test_invalid_jinja2_without_extension():
    j2 = StringIO("{% do navigation.append('a string') %}")
    j2.name = "path/to/file"
    assert not jinja2_validation_result(j2).passed


def test_valid_toml():
    toml = StringIO('a = "b"')
    toml.name = "path/to/file"
    assert toml_validation_result(toml).passed


def test_invalid_toml():
    toml = StringIO("a = b")
    toml.name = "path/to/file"
    assert not toml_validation_result(toml).passed
