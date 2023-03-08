from setuptools import setup
from myfirstmodule import __version__

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
setup(
    name='myfirstmodule',
    version=__version__,
    url='https://github.com/samu32ELTE/myfirstmodule/',
    author='Sámuel G. Balogh',
    author_email='samu32@caesar.elte.hu',
    py_modules=['myfirstmodule'],
    install_requires= REQUIREMENTS
)


