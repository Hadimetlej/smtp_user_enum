# filepath: c:\Users\hadi5\OneDrive\Desktop\Machine learning\setup.py
from setuptools import setup, find_packages

setup(
    name="smtp_user_enum",  # Name of your project
    version="1.0.0",  # Version of the project
    description="SMTP User Enumeration Script for enumerating valid usernames on an SMTP server",
    author="Hadi Metlej",
    author_email="hadi531metlej@gmail.com",
    url="https://github.com/Hadimetlej/smtp_user_enum",  # Project URL
    packages=find_packages(),
    install_requires=[
        "colorama==0.4.4",
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            'smtp_user_enum = smtp_user_enum.smtp_user_enum:main',  # Entry point for the script
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
