import pynetoptix
import random
import json
import time

event_rule_id = '{39628a23-1044-4357-a102-85953c9cb90d}'

client = pynetoptix.create_client('admin', 'IIavaOP512', '10.1.242.178')
action_type = 'showTextOverlayAction'
action_params = {
    'allUsers': False,
    'durationMs': 5000,
    'forced': True,
    'fps': 10,
    'needConfirmation': False,
    'streamQuality': 'highest',
    'text': None,
}
event_rule_comment = 'CUSTOM_AVA_OP_EVENT_RULE_1'

print(client.server.create_event_rule(action_type, action_params, event_rule_comment))

from pprint import pprint
pprint(client.server.get_event_rules())

# rule = [r for r in client.server.get_event_rules() if r['id'] == event_rule_id][0]
#
# camera_ids = [
#     '{5f960023-4550-b853-881c-e04eeaab67aa}',
#     '{9cef335f-e1b2-caf6-4dc1-979152005ee1}',
#     '{b1ada544-a4f5-2640-3de6-9fdfa5039d5e}',
#     '{c2323c3f-06eb-d712-646a-304015121925}'
# ]
#
#
# def determine_alert_color(confidence):
#     font_color = 'white'
#     if confidence > 0.9:
#         font_color = 'red'
#     elif confidence > 0.8:
#         font_color = 'orange'
#     return font_color
#
#
# def main():
#     while True:
#         confidence = random.random()
#         font_color = determine_alert_color(confidence)
#         camera_id = random.sample(camera_ids, 1)[0]
#
#         action_params = json.loads(rule['actionParams'])
#         action_params['text'] = f'<font color="{font_color}">person: {confidence}</font>'
#         action_params = json.dumps(action_params)
#         rule['actionParams'] = action_params
#         rule['actionResourceIds'] = [camera_id]
#
#         client.server.update_event_rule(rule)
#         client.server.create_event(
#             source=camera_id,
#             caption=f'Alert: Person detected ({confidence})',
#             description='A person was detected by Image Intelligence',
#         )
#         time.sleep(0.25)
#
#
# if __name__ == '__main__':
#     main()
