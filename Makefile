FUNC_TEST_DIR='test/functional'
UNIT_TEST_DIR='test/unit'

NOSETESTS?='nosetests'

set_settings:
	cp -f config/settings.py.sample config/settings.py

test_func: set_settings
	${NOSETESTS} -w ${FUNC_TEST_DIR}

test_unit: set_settings
	${NOSETESTS} -w ${UNIT_TEST_DIR}

test: set_settings test_func test_unit

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '._*' -exec rm -f {} +

clean_env: clean
	rm -r bin include lib local man

init_submodules:
	git submodule init
	git submodule update

update_submodules:
	git submodule foreach git pull

.PHONY: init_submodules update_submodules test_func test_unit test clean
