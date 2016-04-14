from setuptools import setup, find_packages

setup(
    name='your_script',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Click'],
    entry_points='''
        [console_scripts]
        your_script=your_script:cli
    ''',
)
