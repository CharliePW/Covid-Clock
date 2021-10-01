import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "Covid-Clock-pkg-cep234",
    version = "0.0.1",
    author = "Charles Pearman-Wright",
    author_email = "cep234@exeter.ac.uk",
    description = "A webpage that can set announces recent covid news, covid cases, the weather and sets alarms",
    long_description = long_description,
    long_description_content = "text/markdown",
    url = "https://github.com/CharliePW/Covid-Clock",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independant",
    ],
    python_requires = ">= 3.9",
)
