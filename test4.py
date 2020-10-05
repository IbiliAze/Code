import argparse
import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

parser = argparse.ArgumentParser(description='Send Running-Configuration Text file')
parser.add_argument('-l', '--location',  required=True, help='Full path to the running-configuration file')
parser.add_argument('-c', '--company',  required=True, help='Owning company')
parser.add_argument('-s', '--site',  required=True, help='Company site')
parser.add_argument('-n', '--name', required=True, help='Name of the config file to set')
parser.add_argument('-t', '--type',  required=False, help='Device type')
parser.add_argument('-x', '--test',  required=False, help='Do not push to production')
parser.add_argument('-j', '--jumpbox',  required=False, help='IP address of the jumpbox/bastion host')

args = parser.parse_args()


def read_file(location):
    file_string = open(location, 'r').read()
    return file_string


def send_to_api(config_file):
    url = 'https://uv4gdvfrga.execute-api.us-east-1.amazonaws.com/v1/config'
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        'company': args.company,
        'site': args.site,
        'configFile': config_file,
        'configName': args.name,
        'deviceType': args.type,
        'test': args.test,
        'jumpbox': args.jumpbox
    }
    response = requests.post(url=url, headers=headers, json=body, verify=False).json()
    print(response)
    print(json.dumps(response, indent=2))



if __name__ == '__main__':
    send_to_api(read_file(args.location))