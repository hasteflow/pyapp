.PHONY: install venv

install:
	@poetry install

venv:
	@poetry shell
