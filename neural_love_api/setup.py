from setuptools import setup, find_packages

setup(
    name="neural-love-api",
    version="1.0.0",
    packages=find_packages(),
    url="",
    license="MIT",
    author="fuziion_dev",
    author_email="info@fuziion.nl",
    description="Python wrapper for the neural.love image generation API",
    install_requires=[
        "requests"
    ],
)