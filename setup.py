from distutils.core import setup
import py2exe, sympy, PyQt4, sys, string
options = {'py2exe': {"includes": ['sympy', 'PyQt4', 'sys', 'string']}}
setup(console=['Main.py'], options=options,zipfile = None)