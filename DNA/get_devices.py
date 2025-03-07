#!/usr/bin/env python3
"""
Script to authenticate with Cisco DNA Center (Catalyst Center) devnet sandbox
and retrieve a list of devices.
"""

from dnacentersdk import DNACenterAPI
import json
from pprint import pprint

# Cisco DevNet Sandbox credentials
# Always-On Catalyst Center (DNA Center) Sandbox
DNAC_URL = "https://sandboxdnac.cisco.com"
DNAC_USERNAME = "devnetuser"
DNAC_PASSWORD = "Cisco123!"

def main():
    """
    Main function to authenticate and get devices from DNA Center
    """
    print("Connecting to Cisco DNA Center...")
    
    # Create a DNACenterAPI connection object
    # Using verify=False to bypass SSL certificate verification
    api = DNACenterAPI(username=DNAC_USERNAME,
                      password=DNAC_PASSWORD,
                      base_url=DNAC_URL,
                      verify=False)
    
    print("Successfully authenticated with DNA Center")
    
    # Get the list of devices
    print("\nRetrieving list of devices...")
    devices = api.devices.get_device_list()
   
    # Print the devices
    print(f"\nFound {len(devices.response)} devices:")
    print("-" * 80)
    
    for device in devices.response:
        print(f"Device Name: {device.hostname}")
        print(f"Device Type: {device.type}")
        print(f"Management IP: {device.managementIpAddress}")
        print(f"Platform ID: {device.platformId}")
        print(f"Serial Number: {device.serialNumber}")
        print(f"Software Version: {device.softwareVersion}")
        print(f"Up Time: {device.upTime}")
        print(f"Status: {device.reachabilityStatus}")
        print("-" * 80)
    
    # Optionally, you can also print the raw JSON response
    # print("\nRaw JSON response:")
    # print(json.dumps(devices, indent=2))

if __name__ == "__main__":
    main() 