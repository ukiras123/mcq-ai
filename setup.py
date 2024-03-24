from setuptools import find_packages, setup

setup(
    name="mcq-ai",
    version="0.0.1",
    author="Kiran Gautam",
    author_email="ukiras@gmail.com",
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages(),
)