#Napalm test file

from napalm import get_network_driver
#from tabulate import tabulate
import json
from datetime import datetime
from pprint import pprint



t1 = datetime.now()

driver = get_network_driver('ios')
with driver('192.168.1.15','admin', 'cisco',optional_args={'secret':'cisco'}) as device:
	facts = device.get_facts()
	snmp = device.get_snmp_information()
	route = device.get_route_to(destination='0.0.0.0/0')


print(json.dumps(facts,sort_keys=True,indent=4))
print(json.dumps(snmp,sort_keys=True,indent=4))
print(json.dumps(route,sort_keys=True,indent=4))


# ios_driver = get_network_driver("ios")
# ios_config = {
# 	"hostname": "192.168.1.15",
# 	"username": "admin",
# 	"password": "cisco",
# 	"optional_args": {'secret':'cisco'}}
#
# with ios_driver(**ios_config) as ios:
# 	pprint(ios.compliance_report("validate-ios.yml"))