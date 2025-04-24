# 1) Look up your existing SSH key by its label:
data "linode_sshkey" "normalkey" {
  label = "normalkey"
}

# 2) Create the Linode VM
resource "linode_instance" "vm" {
  label   = var.label
  region  = var.region
  type    = var.instance_type
  image   = var.image

  # Inject the public key from your existing "normalkey"
  authorized_keys = [
    data.linode_sshkey.normalkey.ssh_key
  ]

  group = "terraform"
}
