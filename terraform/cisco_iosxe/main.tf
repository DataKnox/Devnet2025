resource "iosxe_interface_loopback" "loopback2" {
  name              = var.loopback.id
  description       = var.loopback.description
  shutdown          = false
  ipv4_address      = var.loopback.ip_address
  ipv4_address_mask = var.loopback.ip_mask
}

# Configure GigabitEthernet1/0/1
resource "iosxe_interface_ethernet" "gig1" {
  type        = var.gigabit_ethernet.type
  name        = var.gigabit_ethernet.name
  description = var.gigabit_ethernet.description
  shutdown    = false
  switchport  = true
}

# Configure VLAN 1 interface
resource "iosxe_interface_vlan" "vlan1" {
  name              = var.vlan.id
  description       = var.vlan.description
  shutdown          = false
  ipv4_address      = var.vlan.ip_address
  ipv4_address_mask = var.vlan.ip_mask
}

# Configure OSPF
resource "iosxe_ospf" "ospf1" {
  process_id = var.ospf.process_id
  router_id  = var.ospf.router_id
  networks   = var.ospf.networks
} 