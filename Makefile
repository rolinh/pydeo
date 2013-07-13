FUNC_TEST_DIR='test/functional'
UNIT_TEST_DIR='test/unit'
#docs:
#	sphinx-build -b html -d build/docs/doctrees docs build/docs/html

test:
	nosetests -w ${FUNC_TEST_DIR}
	nosetests -w ${UNIT_TEST_DIR}

test_all: test_27 test_33

test_27:
	nosetests-2.7 -w ${FUNC_TEST_DIR}
	nosetests-2.7 -w ${UNIT_TEST_DIR}

test_33:
	nosetests-3.3 -w ${FUNC_TEST_DIR}
	nosetests-3.3 -w ${UNIT_TEST_DIR}

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '._*' -exec rm -f {} +

.PHONY: test test_all test_27 test_33 clean
