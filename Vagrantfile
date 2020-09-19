Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/xenial64"
    config.vm.network "private_network", ip: "192.168.33.10"
    config.vm.provider "virtualbox" do |vb|
<<<<<<< HEAD
    config.vm.provision :shell, :inline => "sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config; sudo systemctl restart sshd;", run: "always"
    config.vm.synced_folder "app", "/vagrant"
      vb.memory = "1024"
    end
end
=======
      vb.memory = "1024"
    end
  end
>>>>>>> 32bc1c50b0a5fb52100d141bd9045f3c4ff142f1
