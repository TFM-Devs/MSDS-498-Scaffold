install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
            
format:
	black *.py
    
lint:
	pylint --disable=R,C market_movers_cli.py
	pylint --disable=R,C market_movers_lambda.py

test:
	python -m pytest -vv --cov=hello test_hello.py
    
all: 
	install lint test
