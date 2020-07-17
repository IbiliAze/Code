from netmiko import ConnectHandler


ip = '192.168.0.100'
pw = 'cisco'
user = 'ibi'
secret =''

def run_show_commands(ip, pw, user, secret):
    connection = ConnectHandler(ip=ip, device_type="cisco_ios",
        username=user, port=22, password=pw, secret=secret)
    running_config = connection.send_command('show run')
    version = connection.send_command('show ver')
    ip_interfaces = connection.send_command('show ip int br')
    output = '\n RUNNING CONFIG\n \n' + running_config + '\n**************\n VERSION\n \n' + version +  '\n**************\n IP INTERFACE BRIEF\n \n' + ip_interfaces
    hostname = connection.find_prompt()
    hostname = hostname.replace('#', '')
    file = open(f'{hostname}.txt', 'w')
    file.write(output)
    file.close()

run_show_commands(ip, pw, user, secret)