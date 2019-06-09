#!/usr/bin/env python -W ignore

import requests
import click
import json
from sys import exit

@click.command()
@click.option('--username', default='admin', prompt='FortiOS login', help='Fortios login name', required=True)
@click.option('--password', default='admin', prompt='FortiOS password', hide_input=True, help='Fortios user password', required=True)
@click.option('--host', default='fg.4cloud.io', prompt='FortiOS host', help='Fortios host', required=True)
@click.option('--port', default='8443', prompt='FortiOS port', help='Fortios port', required=True)
@click.option('--new_hostname', prompt='FortiOS new hostname', help='Fortios New Hostname', required=True)
def change_forti_hostname(username, password, host, port, new_hostname):
    s = requests.Session()
    login_request_data = "username=" + username + "&secretkey=" + password + "&ajax=1"
    base_url = "https://" + host + ":" + port 
    put_request_data = {}
    put_request_data['hostname'] = new_hostname

    # 1. Login to the device and obtain cookies
    login_response = s.post(base_url + '/logincheck', verify=False, data=login_request_data)
    if login_response.text == "0" :
        click.echo(click.style("Could not authenticate to the device. Check your credentials", fg='red'))
        s.close()
        exit()
    s.headers.update({'X-CSRFTOKEN' : login_response.cookies['ccsrftoken'].replace('\"', '') })

    # 2. Check current hostname
    get_response = s.get(base_url + '/api/v2/cmdb/system/global/', verify=False )
    if get_response.status_code != requests.codes.ok:
        click.echo(click.style("Could not fetch parameters from the device. Check your Fortigate device", fg='red'))
        s.close()
        exit()
    else:
        click.echo(click.style("Old hostname %s" % get_response.json()['results']['hostname'], fg='green'))

    # 3. Change hostname
    put_response = s.put(base_url + '/api/v2/cmdb/system/global', verify=False, data=json.dumps(put_request_data) )    
    if put_response.json()['status'] != 'success' :
        click.echo(click.style("Hostname update was not successful. Check your Fortigate device", fg='red'))
        print(put_response.text)
        s.close()
        exit()
    else:
        click.echo(click.style("Success", fg='green'))

    # 4. Check if hostname has changed
    get_response = s.get(base_url + '/api/v2/cmdb/system/global/', verify=False )
    if get_response.status_code == requests.codes.ok and get_response.json()['results']['hostname'] == new_hostname:
        click.echo(click.style("Current hostname %s" % get_response.json()['results']['hostname'], fg='yellow'))
    else:
        click.echo(click.style("Current hostname %s" % get_response.json()['results']['hostname'], fg='red'))
        s.close()
        exit()

    # 5. Logout
    logout_response = s.post(base_url + '/logout', verify=False)
    if logout_response.status_code == requests.codes.ok :
        click.echo(click.style("Log out with success", fg='green'))
    else:
        click.echo(click.style("Uups! Something went wrong during logout", fg='red'))
        s.close()
        exit()

    # Close the session
    s.close()

if __name__ == "__main__":
    change_forti_hostname()
