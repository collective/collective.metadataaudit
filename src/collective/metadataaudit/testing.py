# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import collective.metadataaudit


class CollectiveMetadataauditLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.metadataaudit)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.metadataaudit:default')


COLLECTIVE_METADATAAUDIT_FIXTURE = CollectiveMetadataauditLayer()


COLLECTIVE_METADATAAUDIT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_METADATAAUDIT_FIXTURE,),
    name='CollectiveMetadataauditLayer:IntegrationTesting',
)


COLLECTIVE_METADATAAUDIT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_METADATAAUDIT_FIXTURE,),
    name='CollectiveMetadataauditLayer:FunctionalTesting',
)


COLLECTIVE_METADATAAUDIT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_METADATAAUDIT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveMetadataauditLayer:AcceptanceTesting',
)
