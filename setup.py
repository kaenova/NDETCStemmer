import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NDETCStemmer_kaenova",
    version="1.4.3",
    py_modules=["NDETCStemmer"],
    description="Library untuk stemming kata dalam Bahasa Indonesia menggunakan metode Nondeterministic Context",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaenova/NDETCStemmer",
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Text Processing :: Linguistic",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    keywords="linguistic stemming indonesian bahasa",
    install_requires=["nltk", "gensim", "gdown", "checksumdir", "huggingface_hub"],
)
