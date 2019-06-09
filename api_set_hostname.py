#!/usr/bin/env python3 -W ignore

import click
from fortiosapi import FortiOSAPI
from pprint import pprint

@click.command()
@click.option('--username', default='admin', prompt='FortiOS login', help='Fortios login name', required=True)
@click.option('--password', default='admin', prompt='FortiOS password', hide_input=True, help='Fortios user password', required=True)
@click.option('--host', default='fg.4cloud.io', prompt='FortiOS host', help='Fortios host', required=True)
@click.option('--port', default='8443', prompt='FortiOS port', help='Fortios port', required=True)
@click.option('--new_hostname', prompt='FortiOS new hostname', help='Fortios New Hostname', required=True)
def change_forti_hostname(username, password, host, port, new_hostname):
    FG = FortiOSAPI()
    credentials = {
        'host': host + ":" + port,
        'username': username,
        'password': password
    }

    hostname_update_payload = {
        'hostname' : new_hostname
    }
    
    FG.login(**credentials)
    out = FG.get('system', 'global')
    click.echo("Old hostname : {0}".format(out['results']['hostname']))
    FG.set('system', 'global', data=hostname_update_payload )
    # Check new hostname:
    out = FG.get('system', 'global')
    click.echo("New hostname : {0}".format(out['results']['hostname']))
    # logout
    FG.logout()

if __name__ == "__main__":
    change_forti_hostname()
