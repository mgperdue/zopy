# Makefile for Sphinx documentation

.PHONY: help clean html

help:
	@echo "Available commands:"
	@echo "  make html   - Build the HTML documentation"
	@echo "  make clean  - Remove the built documentation"

clean:
	rm -rf build/

html:
	sphinx-build -b html source build/html