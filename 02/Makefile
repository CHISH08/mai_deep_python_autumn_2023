all: venv clear_terminal coverage pylint clean

clear_terminal:
	clear

venv:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "Virtual environment setup complete."

coverage:
	@echo "Running coverage tests..."
	./venv/bin/coverage run -m unittest discover -s . -p "*_test.py"
	./venv/bin/coverage report -m
	@echo "Complete coverage tests..."

pylint:
	./venv/bin/pylint "main.py"

clean:
	@echo "Running clean..."
	rm -rf venv .coverage __pycache__
	@echo "Complete clean..."

.PHONY: venv test coverage clean