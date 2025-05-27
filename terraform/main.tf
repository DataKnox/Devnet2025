# Fetch the existing SSH key from Linode
data "linode_sshkey" "existing_key" {
  label = "normalkey"
}

resource "linode_instance" "ubuntu_server" {
  label           = var.instance_label
  image           = "linode/ubuntu24.04"
  region          = "us-southeast"
  type            = "g6-standard-4"  # 4 shared cores
  root_pass       = var.root_password
  authorized_keys = [data.linode_sshkey.existing_key.ssh_key]
  tags            = var.tags

  # Ensure we have a clean shutdown
  watchdog_enabled = true

  # Add some basic metadata
  metadata {
    user_data = base64encode(<<-EOF
      #!/bin/bash
      apt-get update
      apt-get upgrade -y
      EOF
    )
  }
} 