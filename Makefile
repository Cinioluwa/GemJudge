.PHONY: install run lint clean build package

# Default Python interpreter
PYTHON = python

install:
	$(PYTHON) -m pip install -r requirements.txt

run:
	$(PYTHON) judge2.py

lint:
	$(PYTHON) -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	$(PYTHON) -m flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:
	$(PYTHON) setup.py build

package:
	$(PYTHON) setup.py sdist bdist_wheel

test:
	@echo "No tests implemented yet"

help:
	@echo "Available targets:"
	@echo "  install  - Install dependencies"
	@echo "  run      - Run the application"
	@echo "  lint     - Run flake8 linting"
	@echo "  clean    - Clean build artifacts"
	@echo "  build    - Build the package"
	@echo "  package  - Create distribution packages"
	@echo "  test     - Run tests (not implemented yet)"
	@echo "  help     - Show this help message"
