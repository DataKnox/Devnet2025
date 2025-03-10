import requests
import json

# API Configuration
API_KEY = "67b3b2a31a4a84cfe6e33def17688906941f548b"
BASE_URL = "https://api.meraki.com/api/v1"
ORGANIZATION_NAME = "DevNet Sandbox"

def get_organization_id():
    """Get the organization ID for the specified organization name."""
    headers = {
        "X-Cisco-Meraki-API-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    response = requests.get(f"{BASE_URL}/organizations", headers=headers)
    if response.status_code == 200:
        organizations = response.json()
        for org in organizations:
            if org["name"] == ORGANIZATION_NAME:
                return org["id"]
    return None

def get_network_devices(org_id):
    """Get all devices in the organization's networks."""
    headers = {
        "X-Cisco-Meraki-API-Key": API_KEY,
        "Content-Type": "application/json"
    }
    
    # First, get all networks in the organization
    networks_response = requests.get(f"{BASE_URL}/organizations/{org_id}/networks", headers=headers)
    if networks_response.status_code != 200:
        print(f"Error fetching networks: {networks_response.text}")
        return
    
    networks = networks_response.json()
    
    # Get devices for each network
    for network in networks:
        print(f"\nDevices in network: {network['name']}")
        devices_response = requests.get(f"{BASE_URL}/networks/{network['id']}/devices", headers=headers)
        
        if devices_response.status_code == 200:
            devices = devices_response.json()
            for device in devices:
                print(f"- {device['name']} ({device['model']})")
                print(f"  Serial: {device['serial']}")
                print(f"  MAC: {device['mac']}")
                print(f"  Firmware: {device['firmware']}")
                print(f"  Status: {'Online' if device.get('status') == 'online' else 'Offline'}")
        else:
            print(f"Error fetching devices for network {network['name']}: {devices_response.text}")

def main():
    print(f"Fetching devices for organization: {ORGANIZATION_NAME}")
    
    # Get organization ID
    org_id = get_organization_id()
    if not org_id:
        print(f"Could not find organization: {ORGANIZATION_NAME}")
        return
    
    print(f"Found organization ID: {org_id}")
    
    # Get and display devices
    get_network_devices(org_id)

if __name__ == "__main__":
    main() 