from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class ChronografWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        return Alert(
            resource = payload['id'],
            event = payload['message'],
            environment = 'Production',
            severity= 'critical',
            status = 'open',
            service = ['Resouces']
        )


