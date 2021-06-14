from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class DynatraceWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        return Alert(
            resource = data['ImpactedEntities'][0]['entity'],
            event = data['ProblemTitle'],
            environment='Development',
            severity='critical',
            service = data['ImpactedEntities'][1]['entity'],
            group = 'Web Application',
            value = data['ProblemTitle'],
            text = 'High Alert',
            tags = data['Tags'],
            attributes = [],
            origin='dynatrace',
            raw_data=data['Prob lem URL']
        )


