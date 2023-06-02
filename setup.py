from setuptools import find_packages, setup

setup(
    name="fvpy",
    version="0.1-dev",
    packages=find_packages(
        include=[
            "astropy",
            "PyQt6"
            "matplotlib>=3.4",
            "numpy<1.23",
            "black",
            "flake8",
            "isort",
        ]
    ),
)
