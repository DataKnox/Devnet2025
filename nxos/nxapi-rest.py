import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

switchuser = 'admin'
switchpassword = 'Admin_1234!'

auth_url = 'https://sbx-nxos-mgmt.cisco.com/api/mo/aaaLogin.json'
auth_body = {
    "aaaUser": {
        "attributes": {
            "name": switchuser,
            "pwd": switchpassword
            }
        }
    }
auth_response = requests.post(
    auth_url, json=auth_body, timeout=5, verify=False).json()

token = auth_response['imdata'][0]['aaaLogin']['attributes']['token']

cookies = {}
cookies['APIC-Cookie'] = token
headers = {"content-type": "application/json"}

# Get the list of interfaces
interfaces_url = 'https://sbx-nxos-mgmt.cisco.com/api/node/mo/sys/intf/phys-[eth1/33].json?query-target=self'
body = {
	"l1PhysIf":{
		"attributes":{
			"descr":"Knox Wuz here"
		}
	}
}
interfaces_response = requests.put(
    interfaces_url,json=body, headers=headers, cookies=cookies, verify=False).json()

print(interfaces_response)
