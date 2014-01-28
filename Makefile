APP_DIR=app
CONFIG_DIR=config
LIB_DIR=lib
CTRL_LIB_DIR=${LIB_DIR}/controllers
MDLS_LIB_DIR=${LIB_DIR}/models
TEST_DIR=test
FUNC_TEST_DIR=${TEST_DIR}/functional
UNIT_TEST_DIR=${TEST_DIR}/unit

NOSETESTS?=nosetests
PEP8?=pep8

set_settings:
	cp -f config/settings.py.sample config/settings.py

test_func: set_settings
	${NOSETESTS} -w ${FUNC_TEST_DIR}

test_unit: set_settings
	${NOSETESTS} -w ${UNIT_TEST_DIR}

test: set_settings test_func test_unit

pep8:
	${PEP8} ${APP_DIR} ${CTRL_LIB_DIR} ${MDLS_LIB_DIR} ${CONFIG_DIR} ${TEST_DIR}

clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '._*' -exec rm -f {} +

clean_env: clean
	rm -r ./env
	mkdir env
	touch env/.keep

init_submodules:
	git submodule init
	git submodule update

update_submodules:
	git submodule foreach git pull

.PHONY: init_submodules update_submodules test_func test_unit test pep8 clean
