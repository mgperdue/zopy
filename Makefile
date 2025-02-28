.PHONY: test lint format build docs clean

test:
	pytest

lint:
	flake8 src tests

format:
	black src tests

build:
	python -m build

docs:
	sphinx-build docs/source docs/build

clean:
	rm -rf build dist *.egg-info