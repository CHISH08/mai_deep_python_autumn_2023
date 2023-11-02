all: venv clear_terminal pylint1 coverage1 coverage2 clean

clear_terminal:
	clear

venv:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "Virtual environment setup complete."

coverage1:
	@echo "Running coverage tests..."
	./venv/bin/coverage run -m unittest discover -s . -p "*_test1.py"
	./venv/bin/coverage report -m
	@echo "Complete coverage tests..."

pylint1:
	./venv/bin/pylint "main1.py"

coverage2:
	@echo "Running coverage tests..."
	./venv/bin/coverage run -m unittest discover -s . -p "*_test2.py"
	./venv/bin/coverage report -m
	@echo "Complete coverage tests..."

pylint2:
	./venv/bin/pylint "main2.py"

clean:
	@echo "Running clean..."
	rm -rf venv .coverage __pycache__
	@echo "Complete clean..."

.PHONY: venv test coverage clean