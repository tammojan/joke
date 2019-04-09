from setuptools import setup, find_packages

setup(
        name="joke",
        description="Packaging tutorial during Asterics-Obelics School 2019",
        license="MIT License",
        author="Tammo Jan Dijkema",
        author_email="T.J.Dijkema@gmail.com",
        version="1.0.0",
        packages=find_packages(),
        entry_points={
            'console_scripts': ['joke=joke:print_joke']
            },
        install_requires=[],
        url="http://github.com/tammojan/joke"
)
