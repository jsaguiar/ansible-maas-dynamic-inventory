
#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="ansible-maas-dynamic-inventory",
    version="0.0.1",
    author="jsaguiar",
    author_email="jsaguiar@me.com",
    description="dynamic inventory from maas",
    scripts=['bin/maas_tags', 'bin/maas_hostname'],
    url="https://github.com/jsaguiar/ansible-maas-dynamic-inventories",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
