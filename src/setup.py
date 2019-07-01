import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()


setuptools.setup(
    name='first_,cli',
    version='1.0',
    author='Armando Miani',
    author_email='armando.miani@gmail.com',
    description='First CLI',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    scripts=['first-cli'],
    install_requires=[
        'flask'
    ]
)