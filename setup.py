from setuptools import setup, find_packages

setup(
    name="plot-manager",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    extras_require={
        'test': [
            'PySide2',
            'pytest',
            'pytest-cov',
        ],
    },
) 