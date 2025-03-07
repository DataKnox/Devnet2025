from ncclient import manager
import xmltodict
import sys
from typing import Dict, Any
import xml.dom.minidom

# NETCONF filter for interface information
INTERFACE_FILTER = '''
<filter>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name/>
            <description/>
            <enabled/>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip/>
                    <netmask/>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</filter>
'''

def connect_to_device(host: str, username: str, password: str, port: int = 830) -> manager.Manager:
    """
    Establishes a NETCONF connection to the device.
    """
    try:
        connection = manager.connect(
            host=host,
            port=port,
            username=username,
            password=password,
            hostkey_verify=False,
            device_params={'name': 'csr'}
        )
        return connection
    except Exception as e:
        print(f"Failed to connect to {host}: {str(e)}")
        sys.exit(1)

def get_interfaces(connection: manager.Manager) -> Dict[str, Any]:
    """
    Retrieves interface information using NETCONF.
    """
    try:
        response = connection.get(INTERFACE_FILTER)
        #print(response.xml)
        return xmltodict.parse(response.xml)
    except Exception as e:
        print(f"Failed to retrieve interface information: {str(e)}")
        return {}

def display_interfaces(interfaces_data: Dict[str, Any]) -> None:
    """
    Displays interface information in a format similar to 'show ip int brief'.
    """
    print(interfaces_data)
    print("\nInterface\t\tIP Address\t\tStatus")
    print("-" * 60)
    
    try:
        interfaces = interfaces_data['rpc-reply']['data']['interfaces']['interface']
        if not isinstance(interfaces, list):
            interfaces = [interfaces]
            
        for interface in interfaces:
            name = interface.get('name', 'N/A')
            status = "up" if interface.get('enabled') == 'true' else "down"
            
            ip_address = "not assigned"
            if 'ipv4' in interface and 'address' in interface['ipv4']:
                addresses = interface['ipv4']['address']
                if isinstance(addresses, list):
                    ip_address = addresses[0].get('ip', 'not assigned')
                else:
                    ip_address = addresses.get('ip', 'not assigned')
            
            print(f"{name:<20}{ip_address:<20}{status}")
    
    except KeyError as e:
        print(f"Error parsing interface data: {str(e)}")

def main():
    # Device connection parameters
    device = {
        'host': '192.168.0.101',  # Replace with your device's IP
        'username': 'admin',     # Replace with your username
        'password': 'password',     # Replace with your password
        'port': 830             # Standard NETCONF port
    }
    
    # Establish connection
    with connect_to_device(**device) as conn:
        print(f"Successfully connected to {device['host']}")
        
        # Get and display interface information
        interfaces_data = get_interfaces(conn)
        display_interfaces(interfaces_data)

if __name__ == "__main__":
    main()
