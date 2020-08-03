from setuptools import setup

setup(
    name='ttracker',
    version='0.0.3',
    entry_points={
        'console_scripts': [
            'trackr=tracker:main'
        ]
    }
)