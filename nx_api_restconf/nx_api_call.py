from ncclient import manager
import requests
import json

url = 'http://172.16.1.66/ins'
switchuser = 'cisco'
switchpassword = 'cisco'

myheaders = {'content-type':'application/json-rpc'}

payload = [
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "interface eth2/1",
      "version": 1.2
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "description foo-bar",
      "version": 1.2
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "end",
      "version": 1.2
    },
    "id": 3

  }
]

response = requests.post(url=url,data=json.dumps(payload),headers=myheaders,auth=(switchuser,switchpassword)).json()

