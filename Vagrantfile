# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Base box courtesy of Phusion; contains Puppet for saner provisioning
  config.vm.box = "phusion-trusty"
  config.vm.box_url = "https://oss-binaries.phusionpassenger.com/"\
                      "vagrant/boxes/latest/ubuntu-14.04-amd64-vbox.box"

  # Instead of forwarding ports onto localhost, give the VM its own IP
  config.vm.network "private_network", ip: "192.168.33.10"

  # Enable provisioning with Puppet.
  config.vm.provision "puppet" do |puppet|
    puppet.manifests_path = ""
    puppet.manifest_file  = "manifest.pp"
  end
end
