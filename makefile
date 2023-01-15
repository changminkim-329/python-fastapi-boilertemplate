check-pre-p:
	isort app/ tests/ --multi-line=1 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=80
	black app/ tests/ --line-length=80
	mypy app/ tests/ --show-error-context --pretty --strict --ignore-missing-imports --follow-imports=skip
	pytest tests/ --cache-clear -vv --color=yes
check-pre-c:
	isort app/ tests/ --multi-line=1 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=80
	black app/ tests/ --line-length=80
	mypy app/ tests/ --show-error-context --pretty
hook:
	chmod 744 ./git-hooks/install_hooks.sh
	chmod 744 ./git-hooks/pre-push
	chmod 744 ./git-hooks/pre-commit
	./git-hooks/install_hooks.sh
	

    
check-pre-push: check

.PHONY: check pre-push