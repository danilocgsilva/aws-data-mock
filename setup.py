from setuptools import setup

VERSION = '0.0.1'

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="aws-data-mock",
    version=VERSION,
    description="Mocks json data from aws responses api for testting and privary porpouses",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="test mock privacy aws",
    url="https://github.com/danilocgsilva/aws-data-mock",
    author="Danilo Carlos de Góes Silva",
    author_email="contact@danilocgsilva.me",
    packages=["awsmock"],
    include_package_data=True
)
