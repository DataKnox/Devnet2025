import meraki

# API Configuration
API_KEY = "67b3b2a31a4a84cfe6e33def17688906941f548b"
ORGANIZATION_NAME = "DevNet Sandbox"

def main():
    print(f"Fetching devices for organization: {ORGANIZATION_NAME}")
    
    # Initialize the Meraki dashboard
    dashboard = meraki.DashboardAPI(
        api_key=API_KEY,
        output_log=False,
        print_console=False
    )
    
    try:
        # Get all organizations
        organizations = dashboard.organizations.getOrganizations()
     
        # Find the specific organization
        org_id = None
        for org in organizations:
            if org["name"] == ORGANIZATION_NAME:
                org_id = org["id"]
                break
        
        if not org_id:
            print(f"Could not find organization: {ORGANIZATION_NAME}")
            return
            
        print(f"Found organization ID: {org_id}")
        
        # Get all networks for the organization
        networks = dashboard.organizations.getOrganizationNetworks(org_id)
        
        # Get and display devices for each network
        for network in networks:
            print(f"\nDevices in network: {network['name']}")
            
            try:
                devices = dashboard.networks.getNetworkDevices(network['id'])
                
                for device in devices:
                    print(f"- {device.get('name', 'Unnamed Device')} ({device['model']})")
                    print(f"  Serial: {device['serial']}")
                    print(f"  MAC: {device['mac']}")
                    print(f"  Firmware: {device.get('firmware', 'N/A')}")
                    print(f"  Status: {'Online' if device.get('status') == 'online' else 'Offline'}")
                    
            except meraki.APIError as e:
                print(f"Error fetching devices for network {network['name']}: {str(e)}")
                
    except meraki.APIError as e:
        print(f"Error accessing Meraki Dashboard: {str(e)}")

if __name__ == "__main__":
    main() 