from setuptools import setup
from my_first_module import __version__

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]
setup(
    name='my_first_module',
    version=__version__,
    url='https://github.com/samu32ELTE/my_first_module',
    author='Sámuel G. Balogh',
    author_email='samu32@caesar.elte.hu',
    py_modules=['my_first_module'],
    install_requires= REQUIREMENTS #['numpy']
)