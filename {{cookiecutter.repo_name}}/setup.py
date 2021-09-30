import pathlib
from setuptools import setup, find_packages
import versioneer

HERE = pathlib.Path(__file__).parent

PACKAGE_NAME = '{{ cookiecutter.repo_name }}'
AUTHOR = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
AUTHOR_EMAIL = '{{ cookiecutter.email }}'
URL = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}'

LICENSE = "{{ cookiecutter.open_source_license }}"
DESCRIPTION = "{{ cookiecutter.project_short_description }}"
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
    # package requirements go here
]


setup(
    name=PACKAGE_NAME,
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    license=LICENSE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
