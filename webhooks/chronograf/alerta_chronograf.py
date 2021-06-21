from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class ChronografWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        return Alert(
            resource = payload['Resource'],
            event = payload['Event'],
            environment = payload['Environment'],
            severity= payload['Severity'],
            status = payload['Status'],
            service = payload['Service']
        )


