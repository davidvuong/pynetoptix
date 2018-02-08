#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pynetoptix
import random
import json
import time

rule = [r for r in client.server.get_event_rules() if r['id'] == event_rule_id][0]

camera_ids = [
    '{5f960023-4550-b853-881c-e04eeaab67aa}',
    '{9cef335f-e1b2-caf6-4dc1-979152005ee1}',
    '{b1ada544-a4f5-2640-3de6-9fdfa5039d5e}',
    '{c2323c3f-06eb-d712-646a-304015121925}'
]


def determine_alert_color(confidence):
    font_color = 'white'
    if confidence > 0.9:
        font_color = 'red'
    elif confidence > 0.8:
        font_color = 'orange'
    return font_color


def main():
    while True:
        confidence = random.random()
        font_color = determine_alert_color(confidence)
        camera_id = random.sample(camera_ids, 1)[0]

        action_params = json.loads(rule['actionParams'])
        action_params['text'] = f'<font color="{font_color}">person: {confidence}</font>'
        action_params = json.dumps(action_params)
        rule['actionParams'] = action_params
        rule['actionResourceIds'] = [camera_id]

        client.server.update_event_rule(rule)
        client.server.create_event(
            source=camera_id,
            caption=f'Alert: Person detected ({confidence})',
            description='A person was detected by Image Intelligence',
        )
        time.sleep(0.25)


if __name__ == '__main__':
    main()
