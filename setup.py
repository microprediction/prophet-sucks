import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="prophet-sucks",
    version="1.0.0",
    description="A joke package that re-exports `laplace` from skaters. Use skaters instead.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/skaters",
    author="microprediction",
    author_email="peter.cotton@microprediction.com",
    license="MIT",
    classifiers=[
        "Development Status :: 7 - Inactive",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    packages=["prophet_sucks"],
    python_requires=">=3.10",
    include_package_data=True,
    install_requires=["skaters>=0.10.0"],
)
