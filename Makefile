test:
	python -m pip install --user -r tests/requirements.txt
	python -m pytest -vv -s
	python -m pycodestyle . --max-line-length=119 --exclude venv
