req:
	pip install -r requirements.txt

lib:
	pip install .

upload:
	twine upload dist/*

build:
	rm -fr build/ || true
	rm -fr dist/ || true
	pip uninstall -y NDETCStemmer-kaenova
	python setup.py sdist bdist_wheel