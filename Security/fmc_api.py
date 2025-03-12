#!/usr/bin/env python3

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import sys

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class FMCAPIClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.headers = None
        self.domain_uuid = None
        self.base_url = f"https://{self.host}"
        self.auth_url = f"{self.base_url}/api/fmc_platform/v1/auth/generatetoken"
        
    def authenticate(self):
        """Authenticate with FMC and get authentication token"""
        try:
            response = requests.post(
                self.auth_url,
                auth=(self.username, self.password),
                verify=False
            )
            
            if response.status_code == 204:
                self.headers = {
                    'X-auth-access-token': response.headers.get('X-auth-access-token'),
                    'X-auth-refresh-token': response.headers.get('X-auth-refresh-token')
                }
                self.domain_uuid = response.headers.get('DOMAIN_UUID')
                print("Authentication successful!")
                return True
            else:
                print(f"Authentication failed with status code: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"Authentication error: {str(e)}")
            return False
            
    def get_devices(self):
        """Get list of all devices"""
        if not self.headers:
            print("Not authenticated. Please authenticate first.")
            return None
            
        url = f"{self.base_url}/api/fmc_config/v1/domain/{self.domain_uuid}/devices/devicerecords"
        try:
            response = requests.get(url, headers=self.headers, verify=False)
            return response.json()
        except Exception as e:
            print(f"Error getting devices: {str(e)}")
            return None
            
    def get_deployable_devices(self):
        """Get list of deployable devices"""
        if not self.headers:
            print("Not authenticated. Please authenticate first.")
            return None
            
        url = f"{self.base_url}/api/fmc_config/v1/domain/{self.domain_uuid}/deployment/deployabledevices"
        try:
            response = requests.get(url, headers=self.headers, verify=False)
            return response.json()
        except Exception as e:
            print(f"Error getting deployable devices: {str(e)}")
            return None
            
    def get_access_policies(self):
        """Get list of access policies"""
        if not self.headers:
            print("Not authenticated. Please authenticate first.")
            return None
            
        url = f"{self.base_url}/api/fmc_config/v1/domain/{self.domain_uuid}/policy/accesspolicies"
        try:
            response = requests.get(url, headers=self.headers, verify=False)
            return response.json()
        except Exception as e:
            print(f"Error getting access policies: {str(e)}")
            return None

def main():
    # FMC API credentials
    host = "fmcrestapisandbox.cisco.com"
    username = "knoxkn"
    password = "q82ou&_XgM&21mbE"
    
    # Initialize FMC client
    fmc = FMCAPIClient(host, username, password)
    
    # Authenticate
    if not fmc.authenticate():
        sys.exit(1)
        
    # Get and display devices
    print("\nFetching devices...")
    devices = fmc.get_devices()
    if devices:
        print(json.dumps(devices, indent=2))
        
    # Get and display deployable devices
    print("\nFetching deployable devices...")
    deployable_devices = fmc.get_deployable_devices()
    if deployable_devices:
        print(json.dumps(deployable_devices, indent=2))
        
    # Get and display access policies
    print("\nFetching access policies...")
    access_policies = fmc.get_access_policies()
    if access_policies:
        print(json.dumps(access_policies, indent=2))

if __name__ == "__main__":
    main() 