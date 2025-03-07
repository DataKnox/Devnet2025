#!/usr/bin/env python

from acitoolkit.acitoolkit import Tenant, Session
from acitools import URL, USERNAME, PASSWORD

# Login to the APIC
session = Session(URL, USERNAME, PASSWORD)
resp = session.login()
if not resp.ok:
    print('Could not login to APIC')
    exit()

# Get the tenant
tenant = Tenant('Knoxs_Tenant')

# Delete the tenant
tenant.mark_as_deleted()
resp = tenant.push_to_apic(session)

if resp.ok:
    print(f"Successfully deleted tenant: Knoxs_Tenant")
else:
    print(f"Failed to delete tenant. Status: {resp.status_code}")
    print(f"Error: {resp.text}")
