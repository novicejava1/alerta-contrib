from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class KibanaWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        services = []
        serviceValue = payload['Service']
        services.append(serviceValue)

        severityValue = payload['Severity']
        if severityValue == "1":
            sev = 'critical'

        return Alert(
            resource = payload['Resource'],
            event = payload['Trigger'],
            environment = payload['Environment'],
            severity= sev,
            status = payload['Status'],
            service = services,
            text = payload['Text']
        )


