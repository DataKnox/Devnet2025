terraform {
  required_providers {
    iosxe = {
      source  = "CiscoDevNet/iosxe"
      version = ">=0.4.0"
    }
  }
  required_version = ">= 1.0"
}

provider "iosxe" {
  username = "admin"
  password = "password"
  url      = "https://192.168.0.153"
  insecure = true
} 