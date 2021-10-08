lint:
	flake8 py_moysklad tests
	black py_moysklad tests --check
	test -x `which circleci` && circleci config validate .circleci/config.yml

test:
	py.test

lint-fix:
	isort py_moysklad tests
	black py_moysklad tests
