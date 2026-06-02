from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="stokes-viscometer",
    version="2026.5.1",
    author="Iver Oknes",
    author_email="iver@oknes.no",
    description="A package for visual Stokes' viscometer measurements using images.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.14",
    install_requires=["opencv-python", "numpy", "matplotlib"],
    scripts=["bin/viscometer"],
)
