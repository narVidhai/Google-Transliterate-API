from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text(encoding='utf-8')

setup(
    name="google-transliteration-api",
    version="1.0.3",
    description="Google Transliterate API for Python",
    long_description=README,
    long_description_content_type="text/markdown",
    # url="https://github.com/NarVidhai/Google-Transliteration-API",
    project_urls={
        'Documentation': 'https://narvidhai.github.io/Google-Transliterate-API',
        'Tracker': 'https://github.com/NarVidhai/Google-Transliterate-API/issues',
        'Source': 'https://github.com/NarVidhai/Google-Transliterate-API',
    },
    packages=["google.transliteration"],
    # packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries"
    ],
    keywords='Google Transliterate API - Google Input Tools Transliteration',
    license='MIT',
)
