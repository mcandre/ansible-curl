# ansible-curl: an Ansible playbook for installing/uninstalling cURL

# EXAMPLE

```console
$ ansible-playbook -i hosts.ini playbooks/install-curl.yml

$ curl -s http://icanhazip.com
1.2.3.4

$ ansible-playbook -i hosts.ini playbooks/uninstall-curl.yml

$ command -V curl
-bash: command: curl: not found
```

# RUNTIME REQUIREMENTS

* [Ansible](https://www.ansible.com/)

# BUILDTIME REQUIREMENTS

* [tonixxx](https://github.com/mcandre/tonixxx) 0.0.8
* [Vagrant](https://www.vagrantup.com/)

## Optional

* [make](https://www.gnu.org/software/make/)
* [GNU findutils](https://www.gnu.org/software/findutils/)
* [stank](https://github.com/mcandre/stank) (e.g. `go get github.com/mcandre/stank/...`)
* [Python](https://www.python.org) 3+ (for yamllint)
* [Node.js](https://nodejs.org/en/) (for eclint)

# TEST

```console
$ tonixxx boil
```

# CLEAN

```console
$ tonixxx clean
```
