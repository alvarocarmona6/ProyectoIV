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
    azure.tenant_id = 'ae6fb5a9-e051-4e1c-8033-2130e7dced5e'
    azure.client_id = '31d93005-bde3-46bb-b05f-54cc952f258f'
    azure.client_secret = '2cQEwlkRYmWmVLKVEr6hoEGNi27QWs2kARf8GYKIKBs='
    azure.subscription_id = 'e3ab5955-e0f4-4343-b68f-09a462dd43d7'
    azure.vm_size = "Standard_DS2_v2"
  end

  # configuration of ansible
  config.vm.provision :ansible do |ansible|
    	ansible.playbook = "playbook.yml"
  end

end
