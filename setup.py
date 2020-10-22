import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="trainingsetai",
    version="0.0.1",
    author="Trainingset.ai",
    author_email="contactus@trainingset.ai",
    description="The official Python SDK for Trainingset.ai.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trainingset-ai/trainingsetai-python-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries"
    ],
)
