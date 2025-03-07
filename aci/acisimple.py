#!/usr/bin/env python3
import requests
import json
from urllib3.exceptions import InsecureRequestWarning

# Disable SSL warning messages
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_token(url, username, password):
    """Login to APIC and get a token."""
    login_url = f"{url}/api/aaaLogin.json"
    credentials = {
        "aaaUser": {
            "attributes": {
                "name": username,
                "pwd": password
            }
        }
    }
    
    try:
        response = requests.post(
            login_url,
            json=credentials,
            verify=False  # Disable SSL verification
        )
        response.raise_for_status()
        token = response.json()["imdata"][0]["aaaLogin"]["attributes"]["token"]
        return token
    except requests.exceptions.RequestException as e:
        print(f"Login failed: {e}")
        return None

def get_tenants(url, token):
    """Get list of tenants from APIC."""
    tenant_url = f"{url}/api/class/fvTenant.json"
    headers = {
        "Cookie": f"APIC-Cookie={token}"
    }
    
    try:
        response = requests.get(
            tenant_url,
            headers=headers,
            verify=False
        )
        response.raise_for_status()
        return response.json()["imdata"]
    except requests.exceptions.RequestException as e:
        print(f"Failed to get tenants: {e}")
        return None

def main():
    # APIC connection details
    apic_url = "https://sandboxapicdc.cisco.com"
    username = "admin"
    password = "!v3G@!4@Y"
    
    # Get authentication token
    token = get_token(apic_url, username, password)
    if not token:
        return
    
    # Get list of tenants
    tenants = get_tenants(apic_url, token)
    if tenants:
        print("\nList of Tenants:")
        print("-----------------")
        for tenant in tenants:
            tenant_name = tenant["fvTenant"]["attributes"]["name"]
            print(f"- {tenant_name}")

if __name__ == "__main__":
    main()
