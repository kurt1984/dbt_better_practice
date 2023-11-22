# dbt Cookiecutter template for better dbt practice

Powered by Python library [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/), `Cookiecutter dbt` is a framework for jumpstarting production-ready dbt projects quickly.

Contribution are more than welcome to keep it up to date with the latest dbt best practice 

## Features
* dbt related python packages, see requirements.txt for detail
* ruff linting for python
* SQLFluff linting
* yamllint linting
* pre-commit hooks integrated with dbt-checkpoint
* dbt dept packages including codegen
* READAME.md and dbt_better_practice.md for documentation
* makefile for automation
* minimal dbt example code built-in

## Installation

### Using Cookiecutter CLI

```
pip install "cookiecutter>=1.7.0"
cookiecutter gh:kurt1984/dbt_better_practice

```
the cookiecutter.project_slug will be 
- project folder name
- the name entity inside dbt_project.yml


After installation, can checkout README and Makefile for its functionalities.

## tips for working with cookiecutter
it use Jinja template to render, thus can interfere with dbt jinja, if any. Can edit cookiecutter.json file to add the pattern to _copy_without_render. 