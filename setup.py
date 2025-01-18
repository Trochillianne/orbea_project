from setuptools import setup, find_packages

setup(
    name="orbea_project",
    version="1.0.0",
    description="Una herramienta analítica para analizar datos sobre carreras ciclistas",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Victoria Mestre Runge",
    author_email="vmrunge@uoc.edu",
    url="https://github.com/Trochillianne/orbea_project.git",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    py_modules=["main"],
    include_package_data=True,
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "orbea=main:main",
        ],
    },
)