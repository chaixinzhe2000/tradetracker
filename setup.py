from setuptools import setup

# this file documents the package information, and allows the script to be executable

setup(
    name='tradetracker',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'trade=main:main'
        ]
    }
)