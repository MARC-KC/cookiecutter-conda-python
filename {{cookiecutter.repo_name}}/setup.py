from setuptools import setup
import versioneer

requirements = [
    # package requirements go here
]

setup(
    name='{{ cookiecutter.repo_name }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="{{ cookiecutter.project_short_description }}",
    license="{{ cookiecutter.open_source_license }}",
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=['{{ cookiecutter.package_name }}'],
    install_requires=requirements,
    keywords='{{ cookiecutter.repo_name }}',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
