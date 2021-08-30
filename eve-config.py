from netmiko import ConnectHandler
from pprint import pprint


router1 = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.10',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

router3 = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.14',
    'username': 'admin',
    'password': 'cisco',
    'secret': 'cisco',
    'port': 22,
}

#
# list_commands = ['show ip int br',
#                  'show clock',
#                  'show ip route']
#
#
# def send_show_command(device, commands):
#     result = dict()
#     with ConnectHandler(**device) as ssh:
#         ssh.enable()
#         for command in commands:
#             output = ssh.send_command(command)
#             result[command] = output
#     return result
#
#
#
# output = send_show_command(router1, list_commands)
# pprint(output)
#
# base_ospf = ['router ospf 1',
#              'network 0.0.0.0 0.0.0.0 area 0']

# commandset = ['interface range ethernet 0/1-3',
#               'no shut','wr mem']
#
# def config_interface(device,commands):
#     with ConnectHandler(**device) as router:
#         router.enable()
#         router.config_mode()
#         router.send_config_set(commands)
#
# device_list = [router1,router3]
# for device in device_list:
#     config_interface(device,commandset)










