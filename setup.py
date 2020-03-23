import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rodeo-utils",
    version="0.0.1",
    author="Dmitry Bikmetov",
    author_email="bikdm12@gmail.com",
    description="A parser and a set of useful functions for handling RODEO output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bikdm12/rodeo_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=2.7',
)