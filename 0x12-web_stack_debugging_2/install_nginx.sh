#!/bin/bash

# Update package list
sudo apt update

# Install nginx
sudo apt install -y nginx

# Start nginx service
sudo systemctl start nginx

# Enable nginx to start on boot
sudo systemctl enable nginx

# Check nginx status
echo "Nginx installation complete. Checking nginx status..."
sudo systemctl status nginx
