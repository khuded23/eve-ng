from netmiko import ConnectHandler
from pprint import pprint

#
# '''
# This script is used to login to eve-ng ios devices and configure base parameters like
# ssh, admin login,secret, management vrf etc.
#
# '''

router1 = {
	'device_type': 'cisco_ios_telnet',
	'host': '192.168.1.13',
	"username": "admin",
	"password": "cisco",
	'secret': 'cisco',
	'port': 32769}

router2 = {
	'device_type': 'cisco_ios_telnet',
	'host': '192.168.1.13',
	"username": "admin",
	"password": "cisco",
	'secret': 'cisco',
	'port': 32771}

router3 = {
	'device_type': 'cisco_ios_telnet',
	'host': '192.168.1.13',
	"username": "admin",
	"password": "cisco",
	'secret': 'cisco',
	'port': 32772}

router4 = {
	'device_type': 'cisco_ios_telnet',
	'host': '192.168.1.13',
	"username": "admin",
	"password": "cisco",
	'secret': 'cisco',
	'port': 32773}

device_list= [router1,router2,router3,router4]



def telnet_config(device):
	with ConnectHandler(**device) as router:
		print("Connecting to device",device)
		router.enable()
		router.config_mode()
		router.send_config_from_file('base-configs.txt')



