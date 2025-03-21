from setuptools import setup, find_packages

setup(
    name="smtp_user_enum",  # Name of your project
    version="1.0.0",  # Version of the project
    description="SMTP User Enumeration Script for enumerating valid usernames on an SMTP server",
    author="Hadi Metlej",  
    author_email="hadi531metlej@gmai.com",  s
    url="https://github.com/yourusername/smtp_user_enum",  # Project URL (replace with your GitHub or website URL)
    packages=find_packages(),  
    install_requires=[  
        "colorama",  
    ],
    entry_points={  # Create a command-line script entry point
        'console_scripts': [
            'smtp_user_enum = smtp_user_enum:main',  # Replace with the function name to run the script
        ],
    },
    classifiers=[  # Optional: Some classifiers that give metadata about the package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Minimum Python version required
)
