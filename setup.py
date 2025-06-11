from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-code-evaluator",
    version="0.1.0",
    author="",
    author_email="",
    description="A tool for evaluating Python code submissions using Google's Gemini AI API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/python-code-evaluator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "google-generativeai>=0.3.0",
        "customtkinter>=5.2.0",
        "CTkMessagebox>=2.5",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "python-evaluator=judge2:main",
        ],
    },
)
