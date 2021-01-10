from os import environ
import logging

# todo: for debug only. remove in prod.
environ['DISABLE_VERSION_CHECK'] = 'true'

from openbrokerapi import api
from openbrokerapi.catalog import ServiceMetadata, ServicePlan
from openbrokerapi.service_broker import (
    ServiceBroker,
    UnbindDetails,
    BindDetails,
    Binding,
    DeprovisionDetails,
    DeprovisionServiceSpec,
    ProvisionDetails,
    ProvisionedServiceSpec,
    Service,
    UnbindSpec)

logger = logging.getLogger(__name__)


class Broker(ServiceBroker):
    """
    This class should be implemented.

    The minimum setup to register a service broker requires the `catalog()`.
    To create and delete a service instance `provision` and `deprovision` are required.
    To bind and unbind a service instance you have to implement `bind` and `unbind` in addition.

    If some steps are async, you will have to add further methods. Please have a look in the Open Service Broker Spec.
    """

    def __init__(self):
        pass

    kaka = {

        'plans': [{'name': 'satellite-iaas-plan',
                   'free': False,
                   'description': 'Satellite Infrastructure Services plan',
                   'id': 'd88b26d9-0497-4351-8691-3e3bec9110fb',
                   'metadata': {'regional': True,
                                'subscription': False,
                                'paidOnly': False,
                                'allowInternalUsers': False,
                                'reservable': False,
                                'subscriptionOnly': False,
                                'displayName': 'Satellite Infrastructure Services plan',
                                'bullets': ['Satellite Infrastructure Services plan'],
                                'costs': [{'partNumber': 'part-satellite-iaas',
                                           'unit': 'Virtual Processor Core-Hour',
                                           'unitId': 'VIRTUAL_PROCESSOR_CORE_HOURS',
                                           'resourceDisplayName': 'VIRTUAL_PROCESSOR_CORE_HOURS',
                                           'rating_model': 'linear_tier',
                                           'rating_scale': 1,
                                           'free_units': 0,
                                           'instance_free_units': 0,
                                           'scale': 1,
                                           'is_rated': True,
                                           'model': 'standard_add',
                                           'rmcGenTime': 1607014667355},
                                          {'partNumber': 'part-satellite-iaas-blockfile.silver',
                                           'unit': 'Gigabyte-Hour',
                                           'unitId': 'GIGABYTE_HOURS',
                                           'resourceDisplayName': 'GIGABYTE_HOURS',
                                           'rating_model': 'linear_tier',
                                           'rating_scale': 1,
                                           'free_units': 0,
                                           'instance_free_units': 0,
                                           'scale': 1,
                                           'is_rated': True,
                                           'model': 'standard_add',
                                           'rmcGenTime': 1607014675809}]},
                   'pricingCatalogRev': '1-b0bb34480087ba8c8ae8e5ebc5b20511',
                   'pricingCatalogId': 'a519026390e751bf3f0bc401840152c8'}]}
    CATALOG = {'metadata': {'type': 'public',
                            'longDescription': 'Satellite Infrastructure Service offering for IBM Cloud Satellite',
                            'serviceKeysSupported': False,
                            'displayName': 'Satellite Infrastructure Service ',
                            'providerDisplayName': 'GTS',
                            'featuredImageUrl': 'https://globalcatalog.test.cloud.ibm.com/api/v1/bd517bf0-88ba-11ea-a52e-91aeb42a4019/artifacts/satellite-appIcon_lightTheme.svg',
                            'documentationUrl': 'https://www.ibm.com/cloud/satellite',
                            'termsUrl': 'https://www-03.ibm.com/software/sla/sladb.nsf/sla/bm-6605-19',
                            'catalogDetailsUrl': '',
                            'parameters': [],
                            'imageUrl': 'https://globalcatalog.test.cloud.ibm.com/api/v1/bd517bf0-88ba-11ea-a52e-91aeb42a4019/artifacts/satellite-appIcon_lightTheme.svg',
                            'smallImageUrl': 'https://globalcatalog.test.cloud.ibm.com/api/v1/bd517bf0-88ba-11ea-a52e-91aeb42a4019/artifacts/satellite-appIcon_lightTheme.svg',
                            'mediumImageUrl': 'https://globalcatalog.test.cloud.ibm.com/api/v1/bd517bf0-88ba-11ea-a52e-91aeb42a4019/artifacts/satellite-appIcon_lightTheme.svg',
                            'supportUrl': 'https://cloud.ibm.com/unifiedsupport/supportcenter'},
               'bindable': False,
               'rc_compatible': True,
               'iam_compatible': False,
               'plan_updateable': False,
               'unique_api_key': False,
               'tags': ['rc_compatible', 'ibm_created'],
               'name': 'satellite-iaas',
               'id': 'satellite-iaas',
               'description': 'Satellite Infrastructure Service offering for IBM Cloud Satellite',
               'provisionable': False,
               'plans': [{'name': 'satellite-iaas-plan',
                          'free': False,
                          'description': 'Satellite Infrastructure Services plan',
                          'id': 'd88b26d9-0497-4351-8691-3e3bec9110fb',
                          'metadata': {'regional': True,
                                       'subscription': False,
                                       'paidOnly': False,
                                       'allowInternalUsers': False,
                                       'reservable': False,
                                       'subscriptionOnly': False,
                                       'displayName': 'Satellite Infrastructure Services plan',
                                       'bullets': ['Satellite Infrastructure Services plan'],
                                       'costs': [{'partNumber': 'part-satellite-iaas',
                                                  'unit': 'Virtual Processor Core-Hour',
                                                  'unitId': 'VIRTUAL_PROCESSOR_CORE_HOURS',
                                                  'resourceDisplayName': 'VIRTUAL_PROCESSOR_CORE_HOURS',
                                                  'rating_model': 'linear_tier',
                                                  'rating_scale': 1,
                                                  'free_units': 0,
                                                  'instance_free_units': 0,
                                                  'scale': 1,
                                                  'is_rated': True,
                                                  'model': 'standard_add',
                                                  'rmcGenTime': 1607014667355},
                                                 {'partNumber': 'part-satellite-iaas-blockfile.silver',
                                                  'unit': 'Gigabyte-Hour',
                                                  'unitId': 'GIGABYTE_HOURS',
                                                  'resourceDisplayName': 'GIGABYTE_HOURS',
                                                  'rating_model': 'linear_tier',
                                                  'rating_scale': 1,
                                                  'free_units': 0,
                                                  'instance_free_units': 0,
                                                  'scale': 1,
                                                  'is_rated': True,
                                                  'model': 'standard_add',
                                                  'rmcGenTime': 1607014675809}]},
                          'pricingCatalogRev': '1-b0bb34480087ba8c8ae8e5ebc5b20511',
                          'pricingCatalogId': 'a519026390e751bf3f0bc401840152c8'}]}

    # v2/catalog
    def catalog(self) -> Service:
        # s = Service(
        #     id='satellite-iaas',
        #     name='satellite-iaas',
        #     description='Satellite Infrastructure Service offering for IBM Cloud Satellite',
        #     bindable=False,
        #     plans=[ServicePlan(**p) for p in self.CATALOG['plans']],
        #     tags=['rc_compatible', 'ibm_created'],
        #     metadata=ServiceMetadata(**self.CATALOG['metadata']),
        #     plan_updateable=False,
        #     rc_compatible=True,
        #     iam_compatible=False,
        #     unique_api_key=False,
        #     provisionable=False,
        # )
        s = Service(**self.CATALOG)
        return s

    def provision(self, instance_id: str, details: ProvisionDetails, async_allowed: bool,
                  **kwargs) -> ProvisionedServiceSpec:
        pass

    def deprovision(self, instance_id: str, details: DeprovisionDetails, async_allowed: bool,
                    **kwargs) -> DeprovisionServiceSpec:
        pass

    def bind(self, instance_id: str, binding_id: str, details: BindDetails, async_allowed: bool, **kwargs) -> Binding:
        pass

    def unbind(self, instance_id: str, binding_id: str, details: UnbindDetails, async_allowed: bool,
               **kwargs) -> UnbindSpec:
        pass


def create_broker_blueprint(credentials: api.BrokerCredentials):
    return api.get_blueprint(Broker(), credentials, logger)
