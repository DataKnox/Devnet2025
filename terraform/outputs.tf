output "instance_ip" {
  description = "The public IP address of the Linode instance"
  value       = linode_instance.ubuntu_server.ip_address
}

output "instance_label" {
  description = "The label of the Linode instance"
  value       = linode_instance.ubuntu_server.label
} 