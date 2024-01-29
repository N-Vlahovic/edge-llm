sudo apt-get remove docker

# Add Docker's official GPG key:
if [ -f /etc/apt/keyrings/docker.asc ] then
  sudo apt-get update
  sudo apt-get install ca-certificates curl
  sudo install -m 0755 -d /etc/apt/keyrings
  sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
  sudo chmod a+r /etc/apt/keyrings/docker.asc
else 
  echo 'certificate already exists'
fi

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

# Install the Docker packages:
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Enable docker service:
if systemctl status docker.service | grep -q 'enabled'; then
  echo 'docker service already enabled'
else
  sudo systemctl enable docker.service
  sudo systemctl restart docker.service
fi
if  groups $USER | grep -q 'docker'; then
  echo "$USER already in docker group"
else
  sudo usermod -aG docker $USER
fi
