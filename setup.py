"""Installer for the plone.staticresources package."""

from setuptools import find_packages
from setuptools import setup


long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="plone.staticresources",
    version="2.0.6.dev0",
    description="Static resources for Plone",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Core",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords="Python Plone javascript icons staticresources",
    author="Plone Foundation",
    author_email="plone-developers@lists.sourceforge.net",
    url="https://github.com/plone/plone.staticresources",
    license="GPL version 2",
    packages=find_packages("src", exclude=["ez_setup"]),
    namespace_packages=["plone"],
    package_dir={"": "src"},
    python_requires=">=3.8",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "Products.GenericSetup",
        "setuptools",
        "plone.resource",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
            "plone.testing",
        ],
    },
    entry_points="""
    [console_scripts]
    plone-register-icons = plone.staticresources._scripts.register_icons:main
    plone-register-flags = plone.staticresources._scripts.register_flag_icons:main
    [z3c.autoinclude.plugin]
    target = plone
    """,  # noqa
)
