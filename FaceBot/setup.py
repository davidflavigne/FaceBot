# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from os import path


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
long_description = f.read()

setup(
    name='facebot',
    version='0.1.0',
    description='A Python Bot to connect to facebook',
    long_description=long_description,
    url = '',
    author='David Flavigné',
    author_email='david.flavigne@coding-academy.fr',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5'
    ],
    keywords='sample facebook bot development',
    packages='FaceBot',
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'FaceBot=FaceBot:main',
        ],
    },
)
