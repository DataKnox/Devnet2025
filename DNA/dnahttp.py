#!/usr/bin/env python3
"""
Cisco Catalyst Center API Client
This script provides functions to authenticate and interact with Cisco Catalyst Center APIs
without using the SDK.
"""

import requests
import json
import base64
import time
from requests.auth import HTTPBasicAuth
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

class CatalystCenterAPI:
    """A class for interacting with Cisco Catalyst Center APIs"""
    
    def __init__(self, base_url, username, password, verify=False):
        """
        Initialize the Catalyst Center API client
        
        Args:
            base_url (str): The base URL of the Catalyst Center instance
            username (str): Username for authentication
            password (str): Password for authentication
            verify (bool): Whether to verify SSL certificates
        """
        self.base_url = base_url.rstrip('/')
        self.username = username
        self.password = password
        self.verify = verify
        self.token = None
        self.token_expiry = 0
        
    def authenticate(self):
        """
        Authenticate with Catalyst Center and get a token
        
        Returns:
            bool: True if authentication was successful, False otherwise
        """
        auth_url = f"{self.base_url}/dna/system/api/v1/auth/token"
        
        try:
            response = requests.post(
                auth_url,
                auth=HTTPBasicAuth(self.username, self.password),
                verify=self.verify
            )
            
            response.raise_for_status()
            
            # Extract token from response
            token_data = response.json()
            self.token = token_data.get('Token')
            
            # Set token expiry (tokens typically last for 1 hour)
            self.token_expiry = time.time() + 3600
            
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"Authentication failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return False
    
    def get_headers(self):
        """
        Get headers with authentication token
        
        Returns:
            dict: Headers including the authentication token
        """
        # Check if token is expired or not set
        if self.token is None or time.time() > self.token_expiry:
            self.authenticate()
            
        return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'X-Auth-Token': self.token
        }
    
    def get(self, endpoint, params=None):
        """
        Make a GET request to Catalyst Center
        
        Args:
            endpoint (str): API endpoint to call
            params (dict): Query parameters
            
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.get(
                url,
                headers=self.get_headers(),
                params=params,
                verify=self.verify
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return None
    
    def post(self, endpoint, data=None, json_data=None):
        """
        Make a POST request to Catalyst Center
        
        Args:
            endpoint (str): API endpoint to call
            data (dict): Form data
            json_data (dict): JSON data
            
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.post(
                url,
                headers=self.get_headers(),
                data=data,
                json=json_data,
                verify=self.verify
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return None
    
    def put(self, endpoint, data=None, json_data=None):
        """
        Make a PUT request to Catalyst Center
        
        Args:
            endpoint (str): API endpoint to call
            data (dict): Form data
            json_data (dict): JSON data
            
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.put(
                url,
                headers=self.get_headers(),
                data=data,
                json=json_data,
                verify=self.verify
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"PUT request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return None
    
    def delete(self, endpoint, params=None):
        """
        Make a DELETE request to Catalyst Center
        
        Args:
            endpoint (str): API endpoint to call
            params (dict): Query parameters
            
        Returns:
            dict: Response data
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            response = requests.delete(
                url,
                headers=self.get_headers(),
                params=params,
                verify=self.verify
            )
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"DELETE request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return None


# Example usage
if __name__ == "__main__":
    # Sandbox credentials
    BASE_URL = "https://sandboxdnac.cisco.com"
    USERNAME = "devnetuser"
    PASSWORD = "Cisco123!"
    
    # Initialize the API client
    dnac = CatalystCenterAPI(BASE_URL, USERNAME, PASSWORD)
    
    # Authenticate and get token
    if dnac.authenticate():
        print(f"Authentication successful!")
        print(f"Token: {dnac.token}")
        
        # Example API call - Get network devices
        devices = dnac.get("/dna/intent/api/v1/network-device")
        if devices:
            print(f"\nFound {len(devices.get('response', []))} network devices:")
            for device in devices.get('response', []):
                print(f"- {device.get('hostname')} ({device.get('managementIpAddress')})")
    else:
        print("Authentication failed.")
