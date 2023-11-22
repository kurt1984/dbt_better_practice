# dbt better practice tips

## golden tips
- Having a primary key in each data model is pretty much the one rule you can't break.
[primary-key](https://docs.getdbt.com/terms/primary-key)
[monotonically-increasing](https://docs.getdbt.com/terms/monotonically-increasing)


## pull request template from [dbt](https://docs.getdbt.com/blog/analytics-pull-request-template)

<!---
Provide a short summary in the Title above. Examples of good PR titles:
* "Feature: add so-and-so models"
* "Fix: deduplicate such-and-such"
* "Update: dbt version 0.13.0"
-->

### Description & motivation

<!---
Describe your changes, and why you're making them. Is this linked to an open
issue, a Trello card, or another pull request? Link it here.
-->

### To-do before merge

<!---
(Optional -- remove this section if not needed)
Include any notes about things that need to happen before this PR is merged, e.g.:
- [ ] Change the base branch
- [ ] Update dbt Cloud jobs
- [ ] Ensure PR #56 is merged
-->

### Screenshots:

<!---
Include a screenshot of the relevant section of the updated DAG. You can access
your version of the DAG by running `dbt docs generate && dbt docs serve`.
-->

### Validation of models:

<!---
Include any output that confirms that the models do what is expected. This might
be a link to an in-development dashboard in your BI tool, or a query that
compares an existing model with a new one.
-->

### Changes to existing models:

<!---
Include this section if you are changing any existing models. Link any related
pull requests on your BI tool, or instructions for merge (e.g. whether old
models should be dropped after merge, or whether a full-refresh run is required)
-->

### Checklist:

<!---
This checklist is mostly useful as a reminder of small things that can easily be
forgotten – it is meant as a helpful tool rather than hoops to jump through.
Put an `x` in all the items that apply, make notes next to any that haven't been
addressed, and remove any items that are not relevant to this PR.
-->

- [ ] My pull request represents one logical piece of work.
- [ ] My commits are related to the pull request and look clean.
- [ ] My SQL follows the [dbt Labs style guide](https://github.com/dbt-labs/corp/blob/master/dbt_style_guide.md).
- [ ] I have materialized my models appropriately.
- [ ] I have added appropriate tests and documentation to any new models.
- [ ] I have updated the README file.
      {%- if project.warehouse == 'redshift' %}
- [ ] I have added sort and dist keys to models materialized as tables.
- [ ] I have validated the SQL in any late-binding views.
      {% endif %}

## Materialization strategy

- start with `view`
- when it takes too long to query, switch to `table`
- when it takes too long to build, switch to `incremental`
    - config setup
    {% config( materialized='incremental', unique_key='') %}
    - identify new rows
        -  more to learn from dbt course `Advanced Materializations`



## when to use

- full-refresh

- fail-fast
