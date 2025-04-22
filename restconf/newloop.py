import requests
import json
from requests.auth import HTTPBasicAuth
import urllib3
import os 
from dotenv import load_dotenv

load_dotenv()

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Device details
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
USER = os.getenv('USER')
PASS = os.getenv('PASS')
my_var = os.getenv('MY_NEW_VAR')
print(my_var)
# RESTCONF headers and base URL
HEADERS = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json'
}
BASE_URL = f'https://{HOST}:{PORT}/restconf/data'

# Loopback interface configuration
LOOPBACK_DATA = {
    "ietf-interfaces:interface": {
        "name": "Loopback22",
        "description": "RESTCONF Created Loopback",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "22.22.22.22",
                    "netmask": "255.255.255.255"
                }
            ]
        }
    }
}

def create_loopback():
    """Create a new loopback interface using RESTCONF."""
    
    url = f"{BASE_URL}/ietf-interfaces:interfaces/interface=Loopback22"
    
    try:
        response = requests.put(
            url=url,
            headers=HEADERS,
            auth=HTTPBasicAuth(USER, PASS),
            json=LOOPBACK_DATA,
            verify=False  # Disable SSL verification
        )
        
        if response.status_code in [200, 201, 204]:
            print("Loopback interface created successfully!")
            return True
        else:
            print(f"Failed to create loopback interface. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    create_loopback()
