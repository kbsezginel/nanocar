"""
.....o--o.....nanocar.....o--o.....
Nanocar Python package setup file.
"""
from setuptools import setup, find_packages


setup(
    name="nanocar",
    version="0.1.0",
    description="Nanocar builder library.",
    author="Kutay B. Sezginel",
    author_email="kbs37@pitt.edu",
    url='https://github.com/kbsezginel/nanocar',
    include_package_data=True,
    packages=find_packages(),
    install_requires=['numpy',
                      'angstrom'],
    dependency_links=['git+https://github.com/kbsezginel/angstrom.git@master#egg=angstrom-0'],
    tests_require=[
        'pytest',
        'pytest-cov',
        'pytest-pep8',
        'tox',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],
)
