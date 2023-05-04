req:
	pip install -r requirements.txt

lib:
	pip install .

upload:
	twine upload dist/*

build:
	python setup.py sdist bdist_wheel