"""Config flow for the Excluded component."""
from __future__ import annotations

from homeassistant import config_entries

from .const import DOMAIN


class ExcludedConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Excluded."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""

        # Abort if an instance of this integration already exists
        if self._async_current_entries():
            return self.async_abort(reason="single_instance_allowed")

        return self.async_create_entry(
            title="Excluded",
            data={},
        )
