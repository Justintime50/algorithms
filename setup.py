import setuptools


with open('README.md', 'r') as fh:
    long_description = fh.read()

DEV_REQUIREMENTS = [
    'bandit == 1.7.*',
    'black == 24.*',
    'flake8 == 7.*',
    'isort == 5.*',
    'mypy == 1.11.*',
    'pytest == 8.*',
    'pytest-cov == 4.*',
]

setuptools.setup(
    name='algorithms',
    version='0.1.0',
    description=(
        'Classic algorithms including Fizz Buzz, Bubble Sort, the Fibonacci Sequence, a Sudoku solver, and more.'
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://github.com/justintime50/algorithms',
    author='Justintime50',
    license='MIT',
    packages=setuptools.find_packages(
        exclude=[
            'examples',
            'test',
        ]
    ),
    package_data={'algorithms': ['py.typed']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': DEV_REQUIREMENTS,
    },
    python_requires='>=3.8, <4',
)
