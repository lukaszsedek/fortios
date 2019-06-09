# fortios

### Installation:

```
virtualenv env
source env/bin/activate
pip3 install -r requirements.txt
```

### Usage:

```
python3 -W ignore set_hostname.py --username=<username> --password=<password> --host=<address> --port=<port> --new_hostname=<new hostname>
```

Where:

username - Fortigate device login

password - Fortigate device password

host - address of Fortigate machine

port - Port to connect to Fortigate device. Default 443 (HTTPS)

new_hostname - Given new hostname

### Output:
```
(env) bash-3.2$ python3 -W ignore set_hostname.py --username admin --password=admin --host=localhost --port=8443 --new_hostname=SampleHostname
Old hostname : hostname1
there is no mkey for system/global
there is no mkey for system/global
New hostname : SampleHostname
(env) bash-3.2$ 
```

