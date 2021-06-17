from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class KibanaWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        return Alert(
            resource = payload['Resource'],
            event = payload['Trigger'],
            environment = payload['Environment'],
            severity= payload['Severity'],
            status = payload['Status'],
            service = payload['Service'],
            text = payload['Text']
        )


