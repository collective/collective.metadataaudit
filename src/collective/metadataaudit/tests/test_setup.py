# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.metadataaudit.testing import (
    COLLECTIVE_METADATAAUDIT_INTEGRATION_TESTING  # noqa: E501,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that collective.metadataaudit is properly installed."""

    layer = COLLECTIVE_METADATAAUDIT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.metadataaudit is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.metadataaudit'))

    def test_browserlayer(self):
        """Test that ICollectiveMetadataauditLayer is registered."""
        from collective.metadataaudit.interfaces import (
            ICollectiveMetadataauditLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveMetadataauditLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_METADATAAUDIT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.metadataaudit'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.metadataaudit is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.metadataaudit'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveMetadataauditLayer is removed."""
        from collective.metadataaudit.interfaces import \
            ICollectiveMetadataauditLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveMetadataauditLayer,
            utils.registered_layers())
