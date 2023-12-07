
import os
import sys

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.chdir('..')

sys.path.insert(1, 'pluginsrc')

if not os.path.exists('pluginsrc/dog.py'):
    print("warning: file dog.py not found")
    sys.exit(0)

from dog import dog_proc

dog_proc()


