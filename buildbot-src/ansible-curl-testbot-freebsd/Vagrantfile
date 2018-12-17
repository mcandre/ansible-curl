Vagrant.configure("2") do |config|
    config.vm.box = "mcandre/freebsd"
    config.vm.box_version = "0.0.1"

    # Prepare for vagrant package
    config.ssh.insert_key = false
    config.vm.synced_folder ".", "/vagrant", type: "rsync", disabled: true

    config.vm.provision "shell", path: "bootstrap.sh", privileged: false
end
