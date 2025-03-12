#!/usr/bin/env python3

from fmcapi import *
import json
import sys

def main():
    # FMC API credentials
    host = "fmcrestapisandbox.cisco.com"
    username = "knoxkn"
    password = "q82ou&_XgM&21mbE"

    try:
        # Create FMC connection object
        with FMC(
            host=host,
            username=username,
            password=password,
            autodeploy=False,
            file_logging=False
        ) as fmc:
            print("Successfully connected to FMC!")

            # Get devices
            print("\nFetching devices...")
            devices = DeviceRecords(fmc=fmc)
            device_list = devices.get()
            if device_list:
                print("\nDevices:")
                print(json.dumps(device_list, indent=2))

            # Get access policies
            print("\nFetching access policies...")
            access_policies = AccessPolicies(fmc=fmc)
            policy_list = access_policies.get()
            if policy_list:
                print("\nAccess Policies:")
                print(json.dumps(policy_list, indent=2))

            # Get network objects
            print("\nFetching network objects...")
            networks = Networks(fmc=fmc)
            network_list = networks.get()
            if network_list:
                print("\nNetwork Objects:")
                print(json.dumps(network_list, indent=2))

            # Get security zones
            print("\nFetching security zones...")
            zones = SecurityZones(fmc=fmc)
            zone_list = zones.get()
            if zone_list:
                print("\nSecurity Zones:")
                print(json.dumps(zone_list, indent=2))

            # Get interface groups
            print("\nFetching interface groups...")
            interface_groups = InterfaceGroups(fmc=fmc)
            group_list = interface_groups.get()
            if group_list:
                print("\nInterface Groups:")
                print(json.dumps(group_list, indent=2))

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 