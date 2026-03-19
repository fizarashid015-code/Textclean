
from setuptools import setup, find_packages

setup(
    name="textcleanx",
    version="0.1",
    author="YourName",
    description="Simple NLP text cleaning package",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[],
)
