# ============================================================
# Makefile for Kaggle ML projects
# ============================================================

ENV_NAME = ml_kaggle
PYTHON_VERSION = 3.11
REQ_FILE = requirements.txt

# ============================================================
# Basic setup
# ============================================================

.PHONY: create-env
create-env:
	@echo ">>> Creating Conda environment: $(ENV_NAME)"
	conda create -y -n $(ENV_NAME) python=$(PYTHON_VERSION)

.PHONY: install
install:
	@echo ">>> Activating environment and installing dependencies..."
	conda run -n $(ENV_NAME) pip install -r $(REQ_FILE)

# ============================================================
# Maintenance
# ============================================================

.PHONY: update
update:
	@echo ">>> Updating packages in $(ENV_NAME)..."
	conda run -n $(ENV_NAME) pip install -U -r $(REQ_FILE)

.PHONY: freeze
freeze:
	@echo ">>> Exporting locked requirements..."
	conda run -n $(ENV_NAME) pip freeze > requirements.lock.txt

.PHONY: clean
clean:
	@echo ">>> Removing Conda environment $(ENV_NAME)..."
	conda remove -y -n $(ENV_NAME) --all

.PHONY: info
info:
	@echo ">>> Showing installed packages..."
	conda run -n $(ENV_NAME) pip list
