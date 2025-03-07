import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
from pprint import pprint

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Device configuration
DEVICE_HOST = "devnetsandboxiosxe.cisco.com"
DEVICE_USERNAME = "admin"
DEVICE_PASSWORD = "C1sco12345"

# RESTCONF settings
RESTCONF_BASE_URL = f"https://{DEVICE_HOST}/restconf"
HEADERS = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}

def get_interfaces():
    """
    Retrieve interface details using RESTCONF
    """
    # Use Cisco IOS-XE specific YANG model
    url = f"{RESTCONF_BASE_URL}/data/Cisco-IOS-XE-interfaces-oper:interfaces"
    
    try:
        # Send GET request
        response = requests.get(
            url=url,
            headers=HEADERS,
            auth=HTTPBasicAuth(DEVICE_USERNAME, DEVICE_PASSWORD),
            verify=False  # Disable SSL verification
        )
        
        # Check if request was successful
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching interface data: {e}")
        return None

def display_interfaces(data):
    """
    Display interface information in a clean, tabular format
    """
    if not data or 'Cisco-IOS-XE-interfaces-oper:interfaces' not in data:
        return
    
    # Header
    print("\nInterface Status Summary")
    print("=" * 80)
    print(f"{'Interface':<20} {'IP Address':<16} {'Status':<10} {'Protocol':<10}")
    print("-" * 80)
    
    interfaces = data['Cisco-IOS-XE-interfaces-oper:interfaces'].get('interface', [])
    
    for interface in interfaces:
        name = interface.get('name', 'N/A')
        
        # Get IP address - ipv4 is directly a string in this model
        ip_address = interface.get('ipv4', 'N/A')
        
        # Get status
        admin_status = interface.get('admin-status', '')
        oper_status = interface.get('oper-status', '')
        
        status = 'up' if admin_status == 'if-state-up' else 'admin down'
        protocol = 'up' if oper_status == 'if-oper-state-ready' else 'down'
        
        print(f"{name:<20} {ip_address:<16} {status:<10} {protocol:<10}")

def main():
    # Get interface details
    interfaces_data = get_interfaces()
    
    if interfaces_data:
        display_interfaces(interfaces_data)
    else:
        print("Failed to retrieve interface data")

if __name__ == "__main__":
    main()
