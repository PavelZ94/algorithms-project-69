install:
	poetry install

update:
	poetry update

test:
	python -m unittest discover -s tests -p 'tests.py'
