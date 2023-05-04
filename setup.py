import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
name='NDETCStemmer_kaenova',  
version='1.4.0',
py_modules=['NDETCStemmer'] ,
description="Library untuk stemming kata dalam Bahasa Indonesia menggunakan metode Nondeterministic Context",
long_description=long_description,
long_description_content_type="text/markdown",
url="https://github.com/kaenova/NDETCStemmer",
packages=setuptools.find_packages(),
include_package_data=True,
zip_safe=False,
classifiers=[
	"Programming Language :: Python :: 3",
	'Intended Audience :: Information Technology',
	'Intended Audience :: Science/Research',
	'Topic :: Text Processing :: Linguistic',
],
# What does your project relate to?
keywords='linguistic stemming indonesian bahasa',
install_requires=[
	'nltk',
	'gensim',
	'gdown',
	'checksumdir',
	'huggingface_hub'
]
)