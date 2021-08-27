"""
imports.py
includes code to reference the use of the import clause
"""
import sys
import functools


def init():
    return True


test_import = __import__('sys')
print(test_import.modules)
print(sys.modules)
print(dir())
print(dir(sys))
print(dir(functools))
