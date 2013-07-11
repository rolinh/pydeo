#docs:
#	sphinx-build -b html -d build/docs/doctrees docs build/docs/html
#
#test:
#	python test/testall.py
#
#test_all: test_27 test_33
#
#test_27:
#	python2.7 test/testall.py
#
#test_33:
#	python3.3 test/testall.py
#
clean:
	find . -name '__pycache__' -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '._*' -exec rm -f {} +

#.PHONY: docs test test_all test_27 test_33 clean
.PHONY: clean
