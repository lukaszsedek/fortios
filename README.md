# Introduction

I created two python scripts in order to solve the problem. First one is named `api_set_hostname.py`. The second is `rest_set_hostname.py`. 
"REST" uses a native REST technology, whereas "API" uses fortiosapi python library. 


### Installation:

```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
pip install -r requirements.txt
```

### Usage:

API
```
python3 -W ignore api_set_hostname.py --username=<username> --password=<password> --host=<address> --port=<port> --new_hostname=<new hostname>
or
./api_set_hostname.py
```

REST
```
python -W ignore rest_set_hostname.py --username=<username> --password=<password> --host=<address> --port=<port> --new_hostname=<new hostname>
or
./rest_set_hostname.py
```
Where:

username - Fortigate device login

password - Fortigate device password

host - address of Fortigate machine

port - Port to connect to Fortigate device. Default 443 (HTTPS)

new_hostname - Given new hostname

### Output:
API:
```
(env) bash-3.2$ python3 -W ignore set_hostname.py --username admin --password=admin --host=localhost --port=8443 --new_hostname=SampleHostname
Old hostname : hostname1
there is no mkey for system/global
there is no mkey for system/global
New hostname : SampleHostname
(env) bash-3.2$ 
```
REST:
```
(env) bash-3.2$   ./rest_set_hostname.py
FortiOS login [admin]:
FortiOS password [admin]:
FortiOS host [fg.4cloud.io]:
FortiOS port [8443]:
FortiOS new hostname: BVCSD
Old hostname AAAA
Success
Current hostname BVCSD
Log out with success

```

### Test Environment
I used Fortigate EC2 machine in AWS with t2.small flavour. All parameters (except password) are set to match my AWS EC2 Fortigate machine.
host: fg.4cloud.io
port: 8443
login: admin
password: <ask lukaszsedek [at] gmail.com>
Tested only with REST over HTTPS


### Explanation

Fortigate REST API 6.0.4 uses coookies in order to keep session open and authenticated, so OAuth mechanisms cannot be used. Both scripts have been written in python language.
REST script uses requests library and keeps one session. The rationale behind this was to reuse cookie mechanism for all request/response calls. Without this, every requests should be built from scrach. 

API script leverages another approach with library provided by Fortinet, which hides REST complecity behind the pure python. The benefit of this is the fact that we do not need to care about cookies, REST, etc.

One of the challenges here was to provide simple and robust CLI interface. I used `click` library. 