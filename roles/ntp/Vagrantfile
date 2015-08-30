# Vagrantfile API/syntax version. Don'ddt touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  config.vm.box = "precise32"
  config.vm.box_url = "http://files.vagrantup.com/precise32.box"

  config.vm.network "public_network"

  config.vm.define "localhost" do |precise|
    precise.vm.hostname = "localhost"
  end

  config.vm.provider :virtualbox do |vb|
    vb.name = "ansible-role-ntp"
  end

# This should already be in the box.
$script = <<SCRIPT
apt-get update
apt-get -qq install python python-pycurl python-apt
SCRIPT

  config.vm.provision "shell", inline: $script

  config.vm.provision "ansible" do |ansible|
    ansible.sudo = true
    ansible.playbook = "role.yml"
    ansible.verbose = "v"
    ansible.host_key_checking = false
  end
end
