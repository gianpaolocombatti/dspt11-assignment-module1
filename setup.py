"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""
# Always prefer setuptools over distutils
from setuptools import setup
setup(
    name='dspt11_assignment_gpc',  # Required
    version='0.0.1',  # Required
    author='dspt11',  # Optional
    author_email='gianpaolofcombatti@gmail.com',  # Optional
    keywords='assignment',  # Optional
    packages=['mymodule'],  # Required
    python_requires='>=3.6, <4',
    install_requires=['pandas', 'numpy'],  # Optional
)