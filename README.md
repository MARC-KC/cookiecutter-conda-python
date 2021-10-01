# cookiecutter-conda-python
A [cookiecutter](https://www.github.com/audreyr/cookiecutter "cookiecutter") template for 
conda packages using Python

## Features

 - Automatic versioning with versioneer (requires git annotated tags before it'll work)
 - Ready-made conda recipe found in conda.recipe/meta.yaml
 - Pre-configured for GitHub Actions
 - Coverage report hosted on Codecov.io (activated after first successful CI run, which uploads results)
 - Code analysis with codacy, setup to exclude versioneer and tests (requires activation of project at Codacy)
 - setup.cfg with flake8 opinions and pytest/pytest-cov configuration (including fixed PYTHONHASHSEED)

## Installation

Prior to installing cookiecutter-conda-python, the cookiecutter package must be installed in your environment. This is achieved via the following command::

    $ conda install cookiecutter

With cookiecutter installed, the cookiecutter-conda-python template can be installed with::

    $ cookiecutter https://github.com/jacpete/cookiecutter-conda-python.git

Once cookiecutter clones the template, you will be asked a series of questions related to your project::

    $ full_name [Full Name]: Enter your full name.

    $ email [Email Address]: Enter your email address.

    $ github_username [github_username]: Enter your github username.

    $ repo_name [repository_name]: Enter the name of your project's repository.

    $ package_name [package_name]: Enter the name of your package.

    $ project_short_description [Short description]: Enter a short description about your project.

    $ noarch_python [y]: Should the package be a noarch build archetecture?

    $ open_source_license ["MIT", "BSD", "ISC", "Apache", "GNUv3", "Proprietary"]: Choose a license to use.

    $ anaconda_user [Destination anaconda organization or username]: Enter the name of the anaconda user or organization that you want the GitHub Action to publish to.


## Usage

After answering the questions asked during installation, a conda Python package will be
created in your current working directory. This package will contain a simple CLI script
and the conda recipe necessary to build the application into a conda package.

You'll still need to activate the web services you want to use - they won't be active automatically.

 - __GitHub Actions__: You will need to add a ANACONDA_TOKEN to your secrets to enable the push of the conda package to your chosen Anaconda user
 - __Codecov__: No configuration necessary - project will be created when first successful CI run completes and uploads coverage results
 - __Codacy__: https://support.codacy.com/hc/en-us/articles/207278449-Getting-started-with-Codacy
