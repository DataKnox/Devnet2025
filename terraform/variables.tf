variable "linode_token" {
  description = "Your Linode API token"
  type        = string
  sensitive   = true
}

variable "instance_label" {
  description = "The label for the Linode instance"
  type        = string
  default     = "ubuntu-server"
}

variable "root_password" {
  description = "The root password for the Linode instance"
  type        = string
  sensitive   = true
}

variable "tags" {
  description = "Tags to apply to the Linode instance"
  type        = list(string)
  default     = ["terraform", "ubuntu", "devnet2025"]
} 