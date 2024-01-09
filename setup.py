
import setuptools
from pathlib import Path

# Get the current directory
current_dir = Path(__file__).resolve().parent

# Specify the path to README.md
readme_path = current_dir / "README.md"

# Check if README.md exists before reading
if readme_path.exists():
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = ""

__version__ = "0.0.0"

REPO_NAME = "cnnClassifier"
AUTHOR_USER_NAME = "entbappy"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "entbappy73@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
