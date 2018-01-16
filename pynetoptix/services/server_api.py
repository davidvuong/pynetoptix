# -*- coding: utf-8 -*-
import json
from pynetoptix.core import http


class ServerApi:
    def __init__(self, config):
        self.config = config

    def ping(self):
        return http.get(f'{self.config.endpoint}/api/ping', headers=self.config.headers)

    def create_event(self, **kwargs):
        """Creates a 'generic'/'userDefined' event."""
        endpoint = f'{self.config.endpoint}/api/createEvent'

        if 'source' not in kwargs and 'caption' not in kwargs and 'description' not in kwargs:
            raise ValueError('Either source, caption, or description must be set')
        qs = http.parse_qs(**kwargs)
        endpoint = f'{endpoint}?{qs}' if qs else endpoint

        return http.get(endpoint, headers=self.config.headers)

    def create_event_rule(self, action_type, action_params, comment):
        endpoint = f'{self.config.endpoint}/ec2/saveEventRule'
        payload = {
            'actionParams': json.dumps(action_params),
            'actionResourceIds': [],
            'actionType': action_type,  # e.g. 'showTextOverlayAction',
            'aggregationPeriod': 0,
            'comment': comment,
            'disabled': False,
            'eventCondition': '',
            'eventResourceIds': [],
            'eventType': 'UserDefinedEvent',
            'schedule': '',
            'system': False,
        }
        return http.post(endpoint, payload, headers=self.config.headers)

    def get_event_rules(self):
        """Retrieves the entire list of event rules in your Nx Server."""
        endpoint = f'{self.config.endpoint}/ec2/getEventRules'
        return http.get(endpoint, headers=self.config.headers)

    def update_event_rule(self, rule):
        """Updates an existing rule (based on rule.id) found in `rule`.

        @see: https://support.networkoptix.com/hc/en-us/articles/115016055728
        """
        endpoint = f'{self.config.endpoint}/ec2/saveEventRule'
        return http.post(endpoint, payload=rule, headers=self.config.headers)

    def update_event_rule_by_id(self, rule_id, **kwargs):
        """Updates an existing rule given the `rule_id`.

        This behaves a similar way to `update_event_rule` with the exception that rather than taking
        in a rule as a `dict`, it will find the rule by fetching via `get_event_rules`.
        """
        rule = [r for r in self.get_event_rules() if r['id'] == '{' + rule_id + '}']
        if not rule:
            raise ValueError('No rule was found for the given rule_id %s' % rule_id)
        rule = {**rule[0], **kwargs}
        return self.update_event_rule(rule)
