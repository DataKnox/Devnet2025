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
    
    # Get the list of clients
    print("\nRetrieving list of clients...")
    clients = api.clients.get_overall_client_health()

    print(json.dumps(clients, indent=2))

if __name__ == "__main__":
    main()