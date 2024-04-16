from setuptools import setup, find_packages

setup(
    name='clts2vec',
    version='1.0.dev0',
    license='MIT',
    description='Vectorizing Speech Sounds in Phonetic Transcription',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    author='Arne Rubehn',
    author_email='arne.rubehn@uni-passau.de',
    url='https://github.com/calc-project/clts2vec',
    keywords='speech sounds, feature vectors, CLTS',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    py_modules=['clts2vec'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    python_requires='>=3.6',
    extras_require={
        'dev': ["pyclts", 'cltoolkit', 'scikit-learn', 'seaborn', 'numpy', 'matplotlib', 'lingpy'],
        'test': [
            "linse>=0.1.0",
            'pytest>=4.3',
            'pytest-cov',
            'coverage>=4.2',
        ],
    },
)
