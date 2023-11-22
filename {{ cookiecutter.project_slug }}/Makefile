install:
	git init &&\
	python3.11 -m venv venv &&\
		./venv/bin/pip install --upgrade pip &&\
		./venv/bin/pip install -r requirements.txt &&\
	./venv/bin/pre-commit install &&\
	./venv/bin/python3.11 setup.py &&\
	./venv/bin/dbt debug &&\
	./venv/bin/dbt deps

update:
	dbt build &&\
		dbt-osmosis yaml refactor &&\
		dbt docs generate &&\
		# Compute doc coverage, print it and write it to coverage-doc.json file 
		dbt-coverage compute doc --cov-report coverage-doc.json &&\
		# Compute test coverage, print it and write it to coverage-test.json file
		dbt-coverage compute test --cov-report coverage-test.json &&\
		dbt docs serve --port 8001