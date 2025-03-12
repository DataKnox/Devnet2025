#!/usr/bin/env python3

import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
from datetime import datetime

# Disable SSL warnings (since we're using a sandbox with self-signed cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class CiscoISEAPI:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)
        self.verify = False  # Disable SSL verification for sandbox
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def _make_request(self, endpoint, method='GET'):
        """Make HTTP request and handle response"""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method,
            url,
            auth=self.auth,
            headers=self.headers,
            verify=self.verify
        )
        
        # Check if the response is successful
        response.raise_for_status()
        
        # Handle empty responses
        if not response.content:
            return {"message": "No data available"}
            
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"message": "Invalid JSON response", "raw_content": response.text}

    def get_active_sessions(self):
        """Get active sessions from ISE"""
        try:
            return self._make_request('/api/v1/session')
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return {"message": "No active sessions found"}
            raise

    def get_endpoints(self):
        """Get all endpoints from ISE"""
        try:
            return self._make_request('/api/v1/endpoint')
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return {"message": "No endpoints found"}
            raise

    def get_identity_groups(self):
        """Get identity groups from ISE"""
        try:
            return self._make_request('/api/v1/identitygroup')
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                return {"message": "No identity groups found"}
            raise

def main():
    # ISE sandbox credentials
    BASE_URL = "https://devnetsandboxise.cisco.com"
    USERNAME = "readonly"
    PASSWORD = "ISEisC00L"

    # Initialize the ISE API client
    ise = CiscoISEAPI(BASE_URL, USERNAME, PASSWORD)

    try:
        # Get and display active sessions
        print("\n=== Active Sessions ===")
        sessions = ise.get_active_sessions()
        print(json.dumps(sessions, indent=2))

        # Get and display endpoints
        print("\n=== Endpoints ===")
        endpoints = ise.get_endpoints()
        print(json.dumps(endpoints, indent=2))

        # Get and display identity groups
        print("\n=== Identity Groups ===")
        groups = ise.get_identity_groups()
        print(json.dumps(groups, indent=2))

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response status code: {e.response.status_code}")
            print(f"Response text: {e.response.text}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main() 