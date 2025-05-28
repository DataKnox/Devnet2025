variable "device" {
  description = "Device connection details"
  type = object({
    host     = string
    username = string
    password = string
    port     = number
  })
}

variable "loopback" {
  description = "Loopback interface configuration"
  type = object({
    id          = number
    description = string
    ip_address  = string
    ip_mask     = string
  })
}

variable "gigabit_ethernet" {
  description = "GigabitEthernet interface configuration"
  type = object({
    name        = string
    description = string
    type        = string
  })
}

variable "vlan" {
  description = "VLAN interface configuration"
  type = object({
    id          = number
    description = string
    ip_address  = string
    ip_mask     = string
  })
}

variable "ospf" {
  description = "OSPF configuration"
  type = object({
    process_id = number
    router_id  = string
    networks = list(object({
      ip      = string
      wildcard = string
      area    = number
    }))
  })
} 