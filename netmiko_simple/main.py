import time, json
from netmiko import *

with open('listing.json', 'r') as f:
    boxes = json.load(f)

# print(type(boxes))
# print(boxes)
# Test print after importing JSON file with device listing
# print(devices)
# print(type(devices))

# iosv_1 = {
#     "device_type": "cisco_ios",
#     "ip": "172.16.1.61",
#     "username": "cisco",
#     "password": "cisco",
#     "secret": "cisco",
#     "port": 22
# }
devices = [boxes]


# for k,v in devices.items():
#     print(v['ip'])
def netmiko_simple():
    for device in devices:
        # print(device)
        # print(type(device))
        for k, v in device.items():
            # print(v)
            nested_device = [v]
            # print(type(nested_device))
            for data in nested_device:
                output_file = nested_device[0]['ip'] + 'output.txt'
                with open(output_file, 'w') as file:
                    command_list = ['show ip int brief\n', 'show arp\n', 'show int summary\n']
                    for i in command_list:
                        connect = ConnectHandler(**data)
                        output = connect.send_command(i)
                        print('Show arp output from {}'.format(nested_device[0]['ip']))
                        print(output)
                        file.write(output+'\n')


netmiko_simple()
