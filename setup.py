from setuptools import setup, find_packages

setup(
    name='dubnext_db_models',
    version='0.1.0',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        # dependencies here
    ]
)
