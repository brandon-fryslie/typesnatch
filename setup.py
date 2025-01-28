from setuptools import setup, find_packages

setup(
    name='typesnatch',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
        'click',
    ],
    entry_points={
        'console_scripts': [
            'typesnatch=typesnatch.cli:cli',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A brief description of TypeSnatch',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/typesnatch',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
