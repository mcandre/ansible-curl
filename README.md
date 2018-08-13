# ansible-curl: an Ansible playbook for installing/uninstalling cURL

# EXAMPLE

```console
$ ansible-playbook playbooks/install-curl.yml

$ curl -s http://icanhazip.com
1.2.3.4

$ ansible-playbook playbooks/uninstall-curl.yml

$ command -V curl
-bash: command: curl: not found
```

# RUNTIME REQUIREMENTS

* [Ansible](https://www.ansible.com/)

# BUILDTIME REQUIREMENTS

* [tonixxx](https://github.com/mcandre/tonixxx) 0.0.7
* [Vagrant](https://www.vagrantup.com/)

# TEST

```console
$ tonixxx boil
```

# CLEAN

```console
$ tonixxx clean
```
