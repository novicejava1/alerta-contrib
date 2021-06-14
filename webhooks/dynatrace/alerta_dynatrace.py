from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class DynatraceWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        services = []
        serviceValue = payload['ImpactedEntities'][1]['entity'].split('-')[0]
        services.append(serviceValue)

        return Alert(
            resource = payload['ProblemImpact'],
            event = payload['ProblemTitle'],
            environment = 'Production',
            severity= 'critical',
            #status = payload['State']
            service = services
            #group = 'Web Application',
            #value = payload['ProblemTitle'],
            #text = 'High Alert',
            #tags = [payload['Tags']]
            #attributes = [],
        )


