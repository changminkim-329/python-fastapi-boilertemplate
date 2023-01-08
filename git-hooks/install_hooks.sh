#!/usr/bin/env zsh
PROJECT_DIR=$(git rev-parse --show-toplevel)

ln -sf $PROJECT_DIR/git-hooks/pre-push $PROJECT_DIR/.git/hooks/pre-push
ln -sf $PROJECT_DIR/git-hooks/pre-commit $PROJECT_DIR/.git/hooks/pre-commit
