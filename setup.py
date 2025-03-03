from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="zopy",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="ZoPy: A Python client for Zoho APIs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/zopy",
    project_urls={
        "Documentation": "https://github.com/yourusername/zopy",
        "Source": "https://github.com/yourusername/zopy",
        "Issue Tracker": "https://github.com/yourusername/zopy/issues",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
