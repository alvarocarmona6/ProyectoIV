# -*- mode: ruby -*-
# vi: set ft=ruby :

puts ENV["TENANT_ID"]
puts ENV["SUBSCRIPTION_ID"]
puts ENV["CLIENT_ID"]
puts ENV["CLIENT_SECRET"]



Vagrant.configure('2') do |config|
  config.vm.box = 'azure'
  config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box' #Caja base vacia
  # use local ssh key to connect to remote vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'
  config.vm.network "public_network" 
  config.vm.network "forwarded_port", guest: 80, host: 80

  config.vm.provider :azure do |azure, override|


    # configuration needed for Azure
    azure.vm_name = "maquinanbabot"
    azure.tenant_id =  ENV["TENANT_ID"]
    azure.client_id = ENV["CLIENT_ID"]
    azure.client_secret = ENV["CLIENT_SECRET"]
    azure.subscription_id = ENV["SUBSCRIPTION_ID"]
    azure.vm_size = "Standard_DS2_v2"
  end

  # configuration of ansible
  config.vm.provision :ansible do |ansible|
    	ansible.playbook = "playbook.yml"
  end

end
