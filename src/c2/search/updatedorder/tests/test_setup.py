# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from c2.search.updatedorder.testing import (  # noqa: E501
    C2_SEARCH_UPDATEDORDER_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that c2.search.updatedorder is properly installed."""

    layer = C2_SEARCH_UPDATEDORDER_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if c2.search.updatedorder is installed."""
        self.assertTrue(self.installer.is_product_installed("c2.search.updatedorder"))

    def test_browserlayer(self):
        """Test that IC2SearchUpdatedorderLayer is registered."""
        from c2.search.updatedorder.interfaces import IC2SearchUpdatedorderLayer
        from plone.browserlayer import utils

        self.assertIn(IC2SearchUpdatedorderLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = C2_SEARCH_UPDATEDORDER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        if get_installer:
            self.installer = get_installer(self.portal, self.layer["request"])
        else:
            self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstall_product("c2.search.updatedorder")
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if c2.search.updatedorder is cleanly uninstalled."""
        self.assertFalse(self.installer.is_product_installed("c2.search.updatedorder"))

    def test_browserlayer_removed(self):
        """Test that IC2SearchUpdatedorderLayer is removed."""
        from c2.search.updatedorder.interfaces import IC2SearchUpdatedorderLayer
        from plone.browserlayer import utils

        self.assertNotIn(IC2SearchUpdatedorderLayer, utils.registered_layers())
