# denne fila gjør at vi kan laste ned pakken lokalt for å bruke funksjoner i /hjelpefunksjoner
from setuptools import setup, find_packages


with open("README.md", "r", encoding = "utf-8") as file:
    long_description = file.read()

setup(
    name = "quarto-aap-mottakere",
    version = "0.1.0",
    author = "Team-Spenn",
    description = "Pakke for å hente data og plotte data til datafortelling om AAP-mottakere",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    packages=find_packages(),
    python_requires = ">=3.12"
)