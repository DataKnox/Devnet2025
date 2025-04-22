import meraki
import os
from datetime import datetime, timedelta

# Initialize the Meraki SDK
API_KEY = "67b3b2a31a"
dashboard = meraki.DashboardAPI(API_KEY, output_log=False, print_console=False)

def get_organization_id(org_name):
    """Get organization ID for a given organization name."""
    organizations = dashboard.organizations.getOrganizations()
    for org in organizations:
        if org['name'] == org_name:
            return org['id']
    raise ValueError(f"Organization '{org_name}' not found")

def get_network_clients(org_name):
    """Get all clients across all networks in the organization."""
    try:
        # Get organization ID
        org_id = get_organization_id(org_name)
        print(f"\nFound organization: {org_name}")

        # Get all networks for this organization
        networks = dashboard.organizations.getOrganizationNetworks(org_id)
        print(f"Found {len(networks)} networks")

        # Get clients for each network
        all_clients = []
        for network in networks:
            print(f"\nRetrieving clients for network: {network['name']}")
            
            # Get clients active in the last 24 hours
            timespan = 86400  # 24 hours in seconds
            try:
                clients = dashboard.networks.getNetworkClients(
                    network['id'],
                    timespan=timespan,
                    perPage=1000
                )
                print(f"Found {len(clients)} clients in {network['name']}")
                
                for client in clients:
                    client['networkName'] = network['name']
                all_clients.extend(clients)
                
            except meraki.APIError as e:
                print(f"Error getting clients for network {network['name']}: {e}")
                continue

        return all_clients

    except meraki.APIError as e:
        print(f"Meraki API Error: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def print_client_info(clients):
    """Print formatted client information."""
    if not clients:
        print("No clients found or error occurred")
        return

    print(f"\nTotal clients found: {len(clients)}")
    print("\nClient Details:")
    print("-" * 80)
    
    for client in clients:
        print(f"Network: {client.get('networkName', 'N/A')}")
        print(f"Description: {client.get('description', 'N/A')}")
        print(f"MAC: {client.get('mac', 'N/A')}")
        print(f"IP: {client.get('ip', 'N/A')}")
        print(f"Manufacturer: {client.get('manufacturer', 'N/A')}")
        print(f"Last Seen: {client.get('lastSeen', 'N/A')}")
        print("-" * 80)

if __name__ == "__main__":
    org_name = "DevNet Sandbox"
    clients = get_network_clients(org_name)
    print_client_info(clients) 