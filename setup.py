import setuptools


with open("README.md", "r", encoding="utf8") as fp:
    long_description = fp.read()


setuptools.setup(
    name="pywmapi",
    version="1.0.0",
    author="leonardodalink",
    author_email="linkyy2000313@gmail.com",
    description="API for warframe market.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leonardodalinky/pywmapi",
    project_urls={
        "Tracker": "https://github.com/leonardodalinky/pywmapi/issues",
        "Source": "https://github.com/leonardodalinky/pywmapi",
        # "Documentation": "https://packaging.python.org/tutorials/distributing-packages/",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    install_requires=[
        "beautifulsoup4>=4",
        "dacite>=1.6",
        "requests>=2",
    ],
    keywords="warframe market api",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
