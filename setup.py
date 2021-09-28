from roma import console
from setuptools import setup, find_packages


# Specify version
VERSION = '1.0.0.dev1'


# Preprocess
console.show_status('Running setup.py for archima-v' + VERSION + ' ...')
console.split('-')


# Run setup
def readme():
  with open('README.md', 'r') as f:
    return f.read()

# Submodules will be included as package data, specified in MANIFEST.in
setup(
  name='archima',
  packages=find_packages(),
  include_package_data=True,
  version=VERSION,
  description='A package providing tools for 3D reconstruction.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  author='William Ro',
  author_email='walienluo@gmail.com',
  url='https://github.com/WilliamRo/archima',
  download_url='https://github.com/WilliamRo/archima/tarball/v' + VERSION,
  license='Apache-2.0',
  keywords=['3D reconstruction', '3D visualization'],
  install_requires=['numpy'],
  classifiers=[
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 3",
    "Topic :: Utilities",
  ],
)
