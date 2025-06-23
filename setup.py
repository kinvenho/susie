from setuptools import setup, find_packages

setup(
    name="susie",
    version="0.1.0",
    description="A CLI tool to list and manage your last 20 shell commands.",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyperclip",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "susie=susie.cli:main",
        ],
    },
    include_package_data=True,
    python_requires=">=3.7",
)
