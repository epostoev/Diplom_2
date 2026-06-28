# FILE_1 = $(shell find ./tests -name "*.py" -type f)
FILE_1 = $(shell find ./methods -name "*.py" -type f)
# FILE_1 = $(shell find ./locators -name "*.py" -type f)
# FILE_1 = $(shell find ./pages -name "*.py" -type f)
# FILE_1 = data.py
# FILE_1 = conftest.py
# FILE_1 = helpers.py

lint:
	python3 -m flake8 $(FILE_1)

fix:
	python3 -m autopep8 --in-place --aggressive --aggressive $(FILE_1)

test:
	pytest -v -s --alluredir=allure_result

report:
	allure serve allure_result

cov:
	pytest --cov=main

cov-html:
	pytest --cov=main --cov-branch --cov-report=html

install_allure:
	echo 'export JAVA_HOME=~/DISTR/jdk-17.0.19+10/Contents/Home' >> ~/.bash
	echo 'export PATH=$PATH:$JAVA_HOME/bin:~/DISTR/allure-2.40.0/bin' >> ~/.bash
	source ~/.bash