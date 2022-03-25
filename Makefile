PYTHON := python
PROJECT_DIR = .
SRC_DIR := ${PROJECT_DIR}/src
PACKAGE_DIR := ${SRC_DIR}/pywmapi
TEST_DIR := ${PROJECT_DIR}/test

PIPREQS := pipreqs
BLACK := black
FLAKE8 := flake8
ISORT := isort

ifeq ($(OS),Windows_NT)
	RMDIR := rmdir /S /Q
	PYTHONPATHSET := set PYTHONPATH=${SRC_DIR};%PYTHONPATH% &&
else
	RMDIR := rm -rf
	PYTHONPATHSET := PYTHONPATH="${SRC_DIR}:${PYTHONPATH}"
endif

.PHONY: help
help:
	@echo "No target specified."
	@echo "Choose one of the following target:"
	@echo "* install: install the pywmapi package"
	@echo "* build: build the wheel for upload"
	@echo "* test: run the tests"
	@echo "* gen-reqs: generate the requirements.txt"
	@echo "* testpypi: upload to testpypi"
	@echo "* pypi: upload to pypi"
	@echo "* black: format the code by black"
	@echo "* black-check: format the code by black, check only"
	@echo "* isort: sort the imports"
	@echo "* isort-check: sort the imports, check only"
	@echo "* uninstall: uninstall the pywmapi package"
	@echo "* clean: clean all the build & dist cache"
	@echo ""

install: build
	${PYTHON} setup.py install

.PHONY: build
build: clean black
	${PYTHON} -m build

.PHONY: test
test:
	${PYTHONPATHSET} ${PYTHON} -m pytest ${TEST_DIR}

.PHONY: gen-reqs
gen-reqs:
	${PIPREQS} ${SRC_DIR} --savepath ${PROJECT_DIR}/requirements.txt

.PHONY: testpypi
testpypi: clean build
	${PYTHON} -m twine upload --repository testpypi dist/*

.PHONY: pypi
pypi: clean build
	${PYTHON} -m twine upload --repository pypi dist/*

.PHONY: flake8
flake8:
	${PYTHON} -m ${FLAKE8} --max-line-length 100 --count --select=E9,F63,F7,F82 --show-source --statistics

.PHONY: black
black:
	${PYTHON} -m ${BLACK} -l 100 -t py37 src test

.PHONY: black-check
black-check:
	${PYTHON} -m ${BLACK} -l 100 -t py37 --check src test

.PHONY: isort
isort:
	${PYTHON} -m ${ISORT} --profile black -m 3 -l 80 ${PACKAGE_DIR} ${TEST_DIR}

.PHONY: isort-check
isort-check:
	${PYTHON} -m ${ISORT} --profile black -m 3 -l 80 --check ${PACKAGE_DIR} ${TEST_DIR}

.PHONY: uninstall
uninstall:
	${PYTHON} -m pip uninstall -y pywmapi

.PHONY: clean
clean:
	${RMDIR} build/
	${RMDIR} dist/
