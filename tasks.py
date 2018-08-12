import glob
import os
from invoke import run, task


@task
def test():
    run('ansible-playbook playbooks/install-curl.yml')
    run('curl -s http://icanhazip.com')
    run('ansible-playbook playbooks/uninstall-curl.yml')
    run('command -V curl')


@task
def pep8():
    run('pep8 .')


@task
def pylint():
    run('pylint *.py')


@task
def pyflakes():
    run('pyflakes .')


@task
def flake8():
    run('flake8 .')


@task
def ansible_check():
    for f in glob.glob("playbooks%s*.yml" % os.sep):
        run('ansible-playbook --check %s' % f)

    for f in glob.glob("playbooks%s*.yaml" % os.sep):
        run('ansible-playbook --check %s' % f)


@task(pre=[pep8, pylint, pyflakes, flake8, ansible_check])
def lint():
    pass
