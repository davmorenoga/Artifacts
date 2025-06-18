from setuptools import setup, find_packages

setup(
    name="milib-ejemplo",
    version="0.0.2",
    author="David Moreno",
    author_email="davmorenoga@ejemplo.com",
    description="Una librería de prueba para subir a Nexus",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)