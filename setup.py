import sys
from setuptools import setup
from myfirstmodule import __version__


if sys.version_info[:2] < (3, 8):
    error = (
        "Myfirstmodule 2.7+ requires Python 3.8 or later (%d.%d detected). \n"
        "For Python 2.7, please install version 2.2 using: \n"
    )
    sys.stderr.write(error + "\n")
    sys.exit(1)

with open("__init__.py") as fid:
    for line in fid:
        if line.startswith("__version__"):
            version = line.strip().split()[-1][1:-1]
            break

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

if __name__ == "__main__":
    setup(
        name='myfirstmodule',
        version=version,
        url='https://github.com/samu32ELTE/myfirstmodule/',
        author='Sámuel G. Balogh',
        author_email='samu32@caesar.elte.hu',
        py_modules=['myfirstmodule'],
        install_requires= REQUIREMENTS
    )


