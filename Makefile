.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: format
format:
	find . -name '*.py'|grep -v migrations|xargs autoflake --in-place --remove-all-unused-imports --remove-unused-variables
	autopep8 --in-place --aggressive --aggressive **/*.py

.PHONY: test
test:
	#nosetests --all-modules --traverse-namespace --with-coverage --cover-min-percentage=95 --cover-package=dashtat --cover-inclusive --cover-html
	pytest tests

.PHONY: lint
lint:
	pylint --rcfile pylint.rc --disable=missing-docstring --msg-template='{msg_id}:{path}:{symbol}:{line:3d},{column}: {obj}: {msg}' **/*.py

.PHONY: build
build: install test lint test

.PHONY: run
run: run
	python3 -m venv venvs/dashtat
	source /venvs/dashtat/bin/activate
	GITHUB_TOKEN=$$GITHUB_TOKEN ORG=$$ORG gunicorn --bind 0.0.0.0 dashtat:app
