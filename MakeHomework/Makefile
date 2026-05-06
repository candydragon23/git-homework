VENV_DIR = .venv
VENV_PYTHON = $(VENV_DIR)/bin/python3
VENV_PIP = $(VENV_DIR)/bin/pip
VENV_ACTIVATE = . $(VENV_DIR)/bin/activate
FILE ?= app.py

.PHONY: create-structure install-dep install test-pytest venv run clean check-requirements typecheck format check-format check

create-structure:
	mkdir -p src tests docs
	touch src/.gitkeep tests/.gitkeep
	touch docs/DOMAIN.md README.md .gitignore setup.py requirements.txt

venv: $(VENV_DIR)

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)

install-dep: $(VENV_DIR)
	$(VENV_PIP) install -r requirements.txt

install: $(VENV_DIR)
	$(VENV_PIP) install -e .

test-pytest: $(VENV_DIR)
	$(VENV_PYTHON) -m pytest

run: $(VENV_DIR)
	$(VENV_PYTHON) src/$(FILE)

clean:
	rm -rf $(VENV_DIR)

check-requirements: $(VENV_DIR)
	$(VENV_PYTHON) check-deps.py

typecheck: $(VENV_DIR)
	$(VENV_PYTHON) -m mypy src/

format:
	black src/

check-format:
	black --check src/

check: typecheck check-format check-requirements
