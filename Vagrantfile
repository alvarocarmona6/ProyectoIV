Vagrant.configure("2") do |config|
  config.vm.box = "dummy"

  config.vm.define "nbabot" do |host|
    host.vm.hostname = "nbabot"
  end
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "ASIAJTAL3MJQE6WKKX4Q"
    aws.secret_access_key = "7HfyL67tmqWuatfdrTMND7g7D6JzeIkClYwlzTk8"
    aws.session_token = "FQoDYXdzEI3//////////wEaDJqyIgNy6V4X/i88bSKsAUI5AIIfR+CIFgKnHDIrbOacHsCWv4OTpv8sVdeq2428gAF0CkbjxNSMy/CBWOBPrvdrZblFJKKMxNeP1DJPNVcpNUeQ4XI5Qv9MBFhr7kGE9dB742qg0729ctlb6sPQhY4JS+D+ABwRNwRzS+Mfa7U2+HsPWIxpiYBmmkANGkzXyN7L5BzJrcugpohoNiYiU/4ggoWifm/Uo++O7BKLrTOSl6Rxo6BEK4WXemoo1KnZ0QU="
    aws.keypair_name = "millave4"
    aws.region= "us-east-2"
    aws.security_groups = "migruposeguro2"
    aws.instance_type= 't2.micro'
   
    aws.ami = "ami-82f4dae7"

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "millave4.pem"
  end
  
    config.vm.provision :ansible do |ansible|
	ansible.playbook = "ansible.yml"
        ansible.verbose = "vvv"
	ansible.force_remote_user= true
	ansible.host_key_checking=false
  end
end
