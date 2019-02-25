#!/usr/bin/env python3
"""
Library for ecl ekf analysis.
"""

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

CLASSIFIERS = """\
Development Status :: 1 - Planning
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Other
Topic :: Software Development
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Scientific/Engineering :: Mathematics
Topic :: Scientific/Engineering :: Physics
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

# pylint: disable=invalid-name

setup(
    name='ecl_ekf_analysis',
    maintainer="Daniel Agar",
    maintainer_email="daniel@px4.io",
    description="A library for PX4 ecl ekf analysis.",
    long_description=long_description,
    url='git+ssh://git@github.com/Auterion/ecl_ekf_analysis',
    author='Johannes Brand',
    author_email='johannes@auterion.com',
    download_url='git+ssh://git@github.com/ecl_ekf_analysis',
    license='BSD 3-Clause',
    classifiers=[_f for _f in CLASSIFIERS.split('\n') if _f],
    platforms=["Windows", "Linux", "Solaris", "Mac OS-X", "Unix"],
    install_requires=['pyulog', 'matplotlib'],
    tests_require=['pytest'],
    test_suite='pytest',
    package_dir = {'': 'src'},
    packages=find_packages('src'),
    version="0.01",
)