from alerta.models.alert import Alert
from alerta.webhooks import WebhookBase

import json

class DynatraceWebhook(WebhookBase):

    def incoming(self, query_string, payload):

        services = []
        #serviceValue = payload['ImpactedEntities'][1]['entity'].split('-')[0]
        #services.append(serviceValue)

        for entities in payload['ImpactedEntities']:
            serviceValue = entities['name']
            services.append(serviceValue)
        
        tagsList = []
        tagsList.append(payload['Tags'])

        return Alert(
            resource = payload['ProblemImpact'],
            event = payload['ProblemID'],
            environment = 'Production',
            severity= 'critical',
            status = payload['State'].lower(),
            service = services,
            #group = 'Web Application',
            value = payload['ProblemTitle'],
            text = payload['Problem URL'],
            tags = tagsList,
            #attributes = [],
            raw_data=json.dumps(payload, indent=4)
        )


