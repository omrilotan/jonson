from setuptools import setup, find_packages

with open("README.md", "r") as readme:
    long_description = readme.read()

setup(
    name="jonson",
    version="1.1.1",
    author="omrilotan",
    description="out-of-the-box, ready-to-use JSON logger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omrilotan/jonson",
    license="unlicense",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    keywords=['json', 'logger', 'structured logging'],
)
