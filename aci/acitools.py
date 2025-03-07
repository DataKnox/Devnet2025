from acitoolkit.acitoolkit import Session, Tenant, AppProfile, EPG, Context, BridgeDomain, Subnet

# Define credentials
URL = 'https://sandboxapicdc.cisco.com'
USERNAME = 'admin'
PASSWORD = '!v3G@!4@Y'

def get_tenants():
    # Create session object and login
    session = Session(URL, USERNAME, PASSWORD)
    resp = session.login()
    
    if not resp.ok:
        print(f'Login failed! Error: {resp.text}')
        return
    
    # Get and print list of tenants
    tenants = Tenant.get(session)
    print('\nList of Tenants:')
    print('-----------------')
    for tenant in tenants:
        print(tenant.name)

def create_knox_tenant():
    # Create session object and login
    session = Session(URL, USERNAME, PASSWORD)
    resp = session.login()
    
    if not resp.ok:
        print(f'Login failed! Error: {resp.text}')
        return

    # Create Tenant
    tenant = Tenant('Knoxs_Tenant')
    
    # Create Application Profile
    app_profile = AppProfile('Knox_AP', tenant)
    
    # Create Context (VRF)
    context = Context('Knox_VRF', tenant)
    
    # Create Bridge Domain
    bd = BridgeDomain('Knox_BD', tenant)
    bd.add_context(context)
    
    # Add subnet to Bridge Domain
    subnet = Subnet('subnet-1', bd)
    subnet.set_addr('10.0.0.1/24')
    
    # Create EPG
    epg = EPG('Knox_EPG', app_profile)
    epg.add_bd(bd)
    
    # Push the complete configuration to APIC
    resp = tenant.push_to_apic(session)
    
    if resp.ok:
        print("\nSuccessfully created tenant and its components!")
        # Get updated list of tenants to confirm
        get_tenants()
    else:
        print(f"\nFailed to create tenant. Error: {resp.text}")

if __name__ == '__main__':
    create_knox_tenant()