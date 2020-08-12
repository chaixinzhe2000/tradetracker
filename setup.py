from setuptools import setup

setup(
    name='tradetracker',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'trade=main:main'
        ]
    }
)