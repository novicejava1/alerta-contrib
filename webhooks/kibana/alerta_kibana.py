from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class KibanaWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        services = []
        serviceValue = payload['Service']
        services.append(serviceValue)

        return Alert(
            resource = payload['Resource'],
            event = payload['Trigger'],
            environment = payload['Environment'],
            severity= payload['Severity'],
            status = payload['Status'],
            service = services,
            text = payload['Text']
        )


