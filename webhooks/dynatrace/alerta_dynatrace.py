from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class DynatraceWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        data = json.load(payload)
        resource = data['ImpactedEntities'][0]['entity']
        event = data['ProblemTitle']
        environment = data['ProblemImpact']
        severity = data['PID']
        correlate = []
        status = data['State']
        service = data['ImpactedEntities'][1]['entity']
        group = "Web Application"
        value = data['ProblemTitle']
        text = "High Alert"
        tags = data['Tags']
        attributes = []
        origin = []
        alerttype = []
        raw_data = data['Problem URL']

        return Alerta(
            resource = data['ImpactedEntities'][0]['entity']
            event = data['ProblemTitle']
            environment='Development',
            severity='critical'
            service = data['ImpactedEntities'][1]['entity']
            group = 'Web Application'
            value = data['ProblemTitle']
            text = 'High Alert'
            tags = data['Tags']
            attributes = []
            origin='dynatrace'
            raw_data=data['Problem URL']
        )


