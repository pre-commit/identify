REBUILD_FLAG =

.PHONY: minimal
minimal: venv

.PHONY: venv
venv: .venv.touch
	tox --notest -e venv $(REBUILD_FLAG)

.PHONY: test
test: .venv.tox.touch
	tox $(REBUILD_FLAG)

.venv.touch .venv.tox.touch: setup.py requirements-dev.txt
	$(eval REBUILD_FLAG := --recreate)
	touch "$@"

.PHONY: clean
clean:
	find -name '*.pyc' -delete
	find -name '__pycache__' -delete
	rm -rf .tox
	rm -rf venv
	rm -rf .venv.touch
	rm -rf .venv.tox.touch
