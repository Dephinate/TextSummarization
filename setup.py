import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "KehnaKyaChahteHo" # Github repo name
SRC_REPO = "TextSummarizer" # Source code directory in local
AUTHOR_NAME = "Palpendiculal" # Github name
AUTHOR_EMAIL = "varuns.india@gmail.com" # Github email

setuptools.setup(
    name= SRC_REPO,
    version= __version__,
    author= AUTHOR_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python package for NLP application",
    long_description= long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}",
    project_urls = {
    "Bug Tracker":f"https://github.com/{AUTHOR_NAME}/{REPO_NAME}/issues",
    }

)