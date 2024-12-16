from setuptools import setup, find_packages

setup(
    name="NorenApiAsync_Flattrade",
    version="0.0.31",
    author="Nagaraju Gunda",
    author_email="gunda.nagaraju92@gmail.com",
    description="A package for NorenOMS",
    long_description=open("README.md", encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="UNKNOWN",
    packages=find_packages(),
    install_requires=[
        "PyYAML",
        "pandas",
        "requests",
        "websockets",
        "aiohttp",
        "aiodns",
        "httpx[http2]",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Adjust as necessary
)