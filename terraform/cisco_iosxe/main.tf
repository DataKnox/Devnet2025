resource "iosxe_interface_loopback" "loopback2" {
  name              = 2
  description       = "Created by Terraform"
  shutdown          = false
  ipv4_address      = "1.1.1.1"
  ipv4_address_mask = "255.255.255.255"
}

# Configure GigabitEthernet1/0/1
resource "iosxe_interface_ethernet" "gig1" {
  type        = "GigabitEthernet"
  name        = "1/0/1"
  description = "Configured by Terraform"
  shutdown    = false
  switchport  = true
}

# Configure VLAN 1 interface
resource "iosxe_interface_vlan" "vlan1" {
  name              = 1
  description       = "Configured by Terraform"
  shutdown          = false
  ipv4_address      = "192.168.1.153"
  ipv4_address_mask = "255.255.255.0"
}

# Configure OSPF
resource "iosxe_ospf" "ospf1" {
  process_id = 1
  router_id  = "1.1.1.1"
  networks = [{
    ip      = "192.168.1.0"
    wildcard = "0.0.0.255"
    area    = 0
  }]
} 