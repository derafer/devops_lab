import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="permonitoritg",
    version='0.2',
    author="Uladzislau Zubtsou",
    author_email="uladzislau_zubtsou@epam.com",
    description="Example of the test application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    license="MIT"
)
