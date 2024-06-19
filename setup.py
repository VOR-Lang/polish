import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="vorlang-polish",
    version="0.0.2",
    author="Vorlang",
    author_email="me@zanderlewis.dev",
    description="The VOR Programming Language Polisher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    repository="https://github.com/VOR-Lang/polish",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
