import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name = 'monoprompt',
    packages = ["monoprompt"],
    version = '1.0.1',
    license='MIT',
    description = 'Decorate your command-line interface and simplify complex user input with an allowlist or blocklist.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author = 'Rodney Maniego Jr.',
    author_email = 'rod.maniego23@gmail.com',
    url = 'https://github.com/rmaniego/monoprompt',
    download_url = 'https://github.com/rmaniego/monoprompt/archive/v1.0.tar.gz',
    keywords = ['CONSOLE', 'COMMANDLINE', 'INPUT', 'UI'],
    install_requires=[],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6'
)