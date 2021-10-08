import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

REQUIREMENTS = [
    'numpy == 1.*',
]

DEV_REQUIREMENTS = [
    'black',
    'coveralls == 3.*',
    'flake8',
    'isort',
    'pytest == 6.*',
    'pytest-cov == 2.*',
]

setuptools.setup(
    name='algorithms',
    version='0.5.0',
    description='A repo of algorithms.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/algorithms',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=REQUIREMENTS,
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.7',
)
