from setuptools import setup, find_packages

setup(
    name = 'asciiart',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/asciiart.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'This is an ascii art generator.',
    install_requires = ['setuptools'],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "asciiart = asciiart.asciiart:main",
        ]
    }
)
