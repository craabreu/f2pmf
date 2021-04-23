"""
Unit and regression test for the f2pmf package.
"""

# Import package, test suite, and other packages as needed
import f2pmf
# import pytest
import sys
import yaml


def test_f2pmf_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "f2pmf" in sys.modules


def test_variable_serialization():
    variable = f2pmf.Variable('test', 0, 1, True)
    dump = yaml.dump(variable, Dumper=yaml.CDumper)
    object = yaml.load(dump, Loader=yaml.CLoader)
    assert object.__repr__() == "<test in [0, 1], periodic>"
