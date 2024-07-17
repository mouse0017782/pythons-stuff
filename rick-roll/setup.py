from setuptools import setup, find_packages

setup(
    name = "RickRollMarkdownMaker",
    version = "1.0",
    description = "Makes a markdown rickroll link template",
    packages = find_packages(),
    install_requires = ['contextlib']  # Example of external package
)