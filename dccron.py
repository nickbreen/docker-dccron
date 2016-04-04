#!/usr/bin/env python

from sys import stdin
from dockercloud import Events
from subprocess import Popen, PIPE, STDOUT
from json import loads

KEYS = ('type','action','state','user','command')

def process_event(event):
    e = loads(event)
    for js in job_specs:
        if (("*" == js['type'] or js['type'] == e['type']) and
            ("*" == js['action'] or js['action'] == e['action']) and
            ("*" == js['state'] or js['state'] == e['state'])):
            command = ["su", js['user'], "-c", js['command'], "-", e['type'], e['action'], e['resource_uri'], e['state'], e['uuid'], e['datetime']] + e['parents']
            p = Popen(command, stdin=PIPE)
            p.communicate(input=event)[0]

job_specs = [dict(zip(KEYS, line.strip().split(None, len(KEYS)-1))) for line in stdin if not line.lstrip().startswith('#') ]

events = Events()
events.on_message(process_event)
events.run_forever()
