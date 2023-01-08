check:
	isort app/ tests/ --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=120 --check-only
	black app/ tests/ --line-length=80 > /dev/null 2>&1
	mypy app/ tests/ --show-error-context --pretty --strict
	pytest tests/ --cache-clear -vv --color=yes
format:
	isort app/ tests/ -rc -y --multi-line=3 --trailing-comma --force-grid-wrap=0 --use-parentheses --line-width=120
	black app/ tests/ --line-length=80 > /dev/null 2>&1
hook:
	chmod 744 ./git-hooks/install_hooks.sh
	chmod 744 ./git-hooks/pre-push
	chmod 744 ./git-hooks/pre-commit
	./git-hooks/install_hooks.sh
	

    
check-pre-push: check

.PHONY: check pre-push