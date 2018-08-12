BOX_NAMESPACE=mcandre
BOX_BASENAME=ansible-curl-testbot-centos
BOX=$(BOX_BASENAME).box

.PHONY: launch-vm clean-vm clean-boxes clean-vagrant-metadata

launch-vm: Vagrantfile
	vagrant up

clean-vm:
	-vagrant destroy -f

clean-boxes:
	-rm -rf *.box

clean-vagrant-metadata:
	-rm -rf .vagrant

clean: clean-boxes clean-vm clean-vagrant-metadata

$(BOX): clean-boxes clean-vm launch-vm export.Vagrantfile
	vagrant package --output $(BOX) --vagrantfile export.Vagrantfile

import: $(BOX)
	vagrant box add --force --name $(BOX_NAMESPACE)/$(BOX_BASENAME) $(BOX)
