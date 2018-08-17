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

# TEST

```console
$ tonixxx boil
```

# CLEAN

```console
$ tonixxx clean
```
