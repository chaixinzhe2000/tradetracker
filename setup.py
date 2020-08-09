from setuptools import setup

setup(
    name='tradetracker',
    version='0.1.0',
    entry_points={
        'console_scripts': [
            'trade=main:main'
        ]
    }
)