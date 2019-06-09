#!/usr/bin/env python3

import click
from fortiosapi import FortiOSAPI
from pprint import pprint

@click.command()
@click.option('--username', prompt='FortiOS login', help='Fortios login name')
@click.option('--password', prompt='FortiOS password', hide_input=True, help='Fortios user password')
@click.option('--host', prompt='FortiOS host', help='Fortios host')
@click.option('--port', default='443', prompt='FortiOS port', help='Fortios port')
@click.option('--new_hostname', prompt='FortiOS new hostname', help='Fortios New Hostname')
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
