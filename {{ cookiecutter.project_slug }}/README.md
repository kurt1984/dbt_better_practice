# dbt better practice

This is a repo to iteratively improve the practice of dbt using a hospital data and is designed to be used as a reference for other dbt projects.

## Installation and Usage

- Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dev requirements ([dbt](https://www.getdbt.com/), [pre-commit](https://pre-commit.com/))
- Run `pre-commit install` to set up your git hook scripts. This will set your hooks so that the next time you push, pre-commit will be invoked (note: on its first invocation, pre-commit will need to install its own dependencies which may take a minute; these dependencies will be installed outside of your project and will be available from that moment onwards).

### Quick Fixes

- Mac OSX python ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed (\_ssl.c:749)
  bash /Applications/Python\*/Install\ Certificates.command

### Profile

more to follow


### Set up an environment variable

use .env, more to follow 

### Using the project:

Once everything has been setup, try running the following commands:

- dbt debug (if you're having issues)
- dbt deps
- dbt seed
- dbt run
- dbt test

### SQL Styleguide + dbt Best Practices

We follow the [Matt Mazur SQL style guide](https://github.com/mattm/sql-style-guide) and the one by [dbt Labs for dbt-specific behaviors](https://github.com/dbt-labs/corp/blob/main/dbt_style_guide.md).

We also follow the [best practices documented on the dbt website](https://docs.getdbt.com/docs/guides/best-practices/).

SQL and YAML styles are enforced by linters that runs automatically before any commit.

## Working with Pre-Commit

- .pre-commit-config.yaml
  - (currently used) [Montreal Analytics Tutorial](https://blog.montrealanalytics.com/automating-dbt-development-workflows-with-pre-commit-b6c7ca708f7)
- Pre-commit is configured to run various checks automatically when you attempt to push your code. We've overridden the default commit pattern to run on push to make committing small changes easier. When you attempt to push your code the pre-commit hooks will run, and if they pass, the push will succeed; if not there is some sort of issue that needs to be resolved before pushing your changes.
- Pre-commit will only run against changed files to keep its execution as quick as possible.
- On its first execution, pre-commit will install any dependencies it needs into a virtual environment (located outside of this repo); this may take a few minutes on its first run, but every following run will reuse that env and as a result will be much quicker.
- The following tools are installed and orchestrated with pre-commit.

### Working with SQLFluff

- .sqlfluff aka sqlfluff configuration files
  - (currently used) [dbt official](https://docs.getdbt.com/best-practices/how-we-style/2-how-we-style-our-sql)
  - [sqlfluff doc](https://docs.sqlfluff.com/en/stable/configuration.html)
- .sqlfluffignore file
  - (currently used) [Montreal Analytics Tutorial](https://blog.montrealanalytics.com/automating-dbt-development-workflows-with-pre-commit-b6c7ca708f7)
- SQLFluff lint is configured as a pre-commit hook that runs on push, so in most cases no explicit commands are needed. This will only list errors and will not fix any errors if found.
- If you would like to run SQLFluff lint manually, or would like to run it in fix mode, you can do so with the following commands which will run them through pre-commit.
    - in order to do so, uncomment "stages: [manual]" in the .pre-commit-config.yaml
      
```
pre-commit run --hook-stage commit sqlfluff-lint --all-files
pre-commit run --hook-stage manual sqlfluff-fix --all-files
```



### Working with YAMLLint

- .yamllint file
  - (currently used) [Montreal Analytics Tutorial](https://blog.montrealanalytics.com/automating-dbt-development-workflows-with-pre-commit-b6c7ca708f7)
- YAMLLint is configured as a pre-commit, so in most cases no explicit commands are needed. This will only list errors and will not fix any errors if found.
- If you would like to run YAMLLint manually, you can do so with the following command which will run it through pre-commit.

```
pre-commit run --hook-stage push yamllint
```

### Working with dbt-checkpoint

- dbt-checkpoint is configured as a set of pre-commit hooks, so in most cases no explicit commands are needed. These hooks will ensure the dbt project is following standard convention. This will only list errors and will not fix any errors if found.
- If you would like to run dbt-checkpoint manually, you can do so with the following command which will run it through pre-commit.

```
pre-commit run <dbt-checkpoint hook_id> --all-files --hook-stage commit
```

### Working with dbt-coverage

- dbt-coverage is a single CLI tool which checks your dbt project for missing documentation and tests. More info found [here](https://github.com/slidoapp/dbt-coverage).
- The command `dbt docs generate` must be run first.
- Once installed, there are 2 main commands to generate test and doc coverage reports:
  - Test Coverage: `dbt-coverage compute test --cov-report coverage-test.json`
  - Doc Coverage: `dbt-coverage compute docs --cov-report coverage-doc.json`
    - Optionally, you may make the run fail if you add `--cov-fail-under 0.5` (range between 0 and 1) to the end of the command, where 0.5 means you must have at least 50% of all docs/tests covered.
- More advanced commands are available in the docs linked above


## Resources:

- [Montreal Analytics Tutorial](https://blog.montrealanalytics.com/automating-dbt-development-workflows-with-pre-commit-b6c7ca708f7)
- [README.md: The Ultimate Guide](https://tiloid.com/p/readme-md-the-ultimate-guide)
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- [How we structure our dbt projects](https://discourse.getdbt.com/t/how-we-structure-our-dbt-projects/355)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [dbt community](http://community.getbdt.com/) to learn from other analytics engineers
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
- dbt [Release notes](https://github.com/fishtown-analytics/dbt/releases)
