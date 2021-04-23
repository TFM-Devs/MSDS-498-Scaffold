install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
            
format:
	black *.py
    
lint:
	pylint --disable=R,C hello.py
	#pylint --disable=R,C NCAA_Model_Week_2.ipynb

test:
	python -m pytest -vv --cov=hello test_hello.py
    
all: 
	install lint test
