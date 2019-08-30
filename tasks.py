import fnmatch
import glob
import os
from invoke import run, task


@task
def test():
    run('ansible-playbook -i hosts.ini playbooks/install-curl.yml')
    run('curl -s http://icanhazip.com')
    run('ansible-playbook -i hosts.ini playbooks/uninstall-curl.yml')


@task
def safety():
    run('safety check')


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
def yamllint():
    run('yamllint -s .yamllint .')


@task
def ansible_check():
    for f in glob.glob("playbooks%s*.yml" % os.sep):
        run('ansible-playbook --check %s' % f)

    for f in glob.glob("playbooks%s*.yaml" % os.sep):
        run('ansible-playbook --check %s' % f)


@task
def ansible_lint():
    for f in glob.glob("playbooks%s*.yml" % os.sep):
        run('ansible-lint %s' % f)

    for f in glob.glob("playbook%s*.yml" % os.sep):
        run('ansible-lint %s' % f)


@task(pre=[
    safety,
    pep8,
    pylint,
    pyflakes,
    yamllint,
    ansible_check,
    ansible_lint
])
def lint():
    pass
