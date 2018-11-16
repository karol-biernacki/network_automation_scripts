from class_device import device
import paramiko, json, time

with open('listing.json', 'r') as file:
    boxes = json.load(file)

print(boxes['iosv-1']['ip'])
commands = ['show version\n ','config t\n','logging buffered 30000\n','end\n','wr mem\n','show runn | in logging\n']

# device.ip = input('Provide IP')
# username = input('Provide Username')
# password = input('Provide username')


def paramiko_handler():
    for box in boxes:
        output_file_name = box + '_output.txt'
        connection_handler = paramiko.SSHClient()
        connection_handler.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        connection_handler.connect(boxes[box]['ip'], username=boxes[box]['username'], password=boxes[box]['password'],
                                   look_for_keys=False,
                                   allow_agent=False)
        print('Shell Invoked !!!')
        shell = connection_handler.invoke_shell()
        shell.send('term length 0\n')
        time.sleep(2)
        output = shell.recv(53350)
        print(output)
        with open(output_file_name, 'wb') as f:
            for command in commands:
                shell.send(command)
                time.sleep(10)
                output = shell.recv(53350)
                print(output)
                f.write(output)
        shell.close()

paramiko_handler()
# print(device.ip)
# print(device.password)
# print(device.username)
