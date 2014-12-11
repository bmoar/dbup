from setuptools import setup, find_packages

setup(
    name='dbup',
    version='0.0',
    packages=find_packages(),
    package_data={"conf": "dbup/core/conf/*"},
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ci = dbup.cli.entry_point:main',
        ]
    },
    install_requires=[
        'nose',
        'coverage',
        'randomize',
        'factory-boy',
        'fake-factory',
        'cement',
        'psycopg2'
    ],
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Private :: Do Not Upload'
    ],
    dependency_links=[]
)
