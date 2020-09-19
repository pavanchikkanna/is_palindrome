import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="is_palindrome", 
    version="0.0.1",
    author="Pavan R",
    author_email="pavanravikumar1998@gmail.com",
    description="A python module for checking palindrome property in a string ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pavanchikkanna/is_palindrome",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["is_palindrome=is_palindrome.__main__:main"]},
    python_requires='>=3.6',
)