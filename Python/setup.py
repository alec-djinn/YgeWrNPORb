# Preparing “setup.py” script to specify which options do we need in our output
# Works with python_to_EXE.py

from distutils.core import setup
import py2exe , sys, os
 
setup(
    options = {'py2exe': {'bundle_files': 1}},
 
    windows = [{'script': "Client.py"}],
    zipfile = None,
)