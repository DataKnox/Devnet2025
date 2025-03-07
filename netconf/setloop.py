from ncclient import manager
import xml.dom.minidom
from typing import Dict

# NETCONF payload for configuring Loopback2
LOOPBACK_CONFIG = '''
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback1</name>
            <description>Configured by NETCONF</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>13.13.13.13</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
'''

def connect_to_device(device_params: Dict) -> manager.Manager:
    """
    Establishes a NETCONF connection to the device.
    """
    try:
        connection = manager.connect(
            host=device_params['host'],
            port=device_params['port'],
            username=device_params['username'],
            password=device_params['password'],
            hostkey_verify=False,
            device_params={'name': 'csr'}
        )
        return connection
    except Exception as e:
        print(f"Failed to connect to {device_params['host']}: {str(e)}")
        raise

def configure_loopback(connection: manager.Manager) -> None:
    """
    Configures Loopback2 interface with the specified IP address.
    """
    try:
        # Send configuration to the device
        response = connection.edit_config(target='running', config=LOOPBACK_CONFIG)
        
        # Pretty print the response
        print("\nConfiguration Result:")
        print(xml.dom.minidom.parseString(response.xml).toprettyxml())
        
        if response.ok:
            print("\nLoopback2 interface configured successfully!")
        else:
            print("\nFailed to configure Loopback2 interface")
            
    except Exception as e:
        print(f"Error configuring interface: {str(e)}")
        raise

def main():
    # Device connection parameters
    device = {
        'host': '192.168.0.101',  # Replace with your device's IP
        'username': 'admin',      # Replace with your username
        'password': 'password',   # Replace with your password
        'port': 830              # Standard NETCONF port
    }
    
    try:
        # Connect to the device
        with connect_to_device(device) as conn:
            print(f"Successfully connected to {device['host']}")
            
            # Configure the loopback interface
            configure_loopback(conn)
            
    except Exception as e:
        print(f"Script execution failed: {str(e)}")

if __name__ == "__main__":
    main()
