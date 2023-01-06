typehint:
	mypy app/	tests/	
test:
	pytest tests/
sort:
	isort app/ tests/ --profile black
 
checklist-pre-commit: sort typehint test

.PHONY: sort typehint test checklist-pre-commit