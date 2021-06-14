from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class DynatraceWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        return Alert(
            resource = payload['ImpactedEntities'][0]['entity'],
            event = payload['ProblemTitle'],
            environment='Development',
            severity='critical',
            service = ['docker']
            #group = 'Web Application',
            #value = payload['ProblemTitle'],
            #text = 'High Alert',
            #tags = payload['Tags']
            #attributes = [],
        )


