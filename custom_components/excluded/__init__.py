"""Excluded actions integration for Home Assistant."""

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, ServiceCall
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers.service import async_extract_referenced_entity_ids

from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Excluded integration."""
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Excluded from a config entry."""

    async def _handle_domain_entities(call: ServiceCall, action: str, domain: str):
        """Handle action calls for a given domain."""
        targeted_data = async_extract_referenced_entity_ids(hass, call)
        # Get all entities that should be excluded (including indirect references)
        excluded = list(targeted_data.referenced) + list(
            targeted_data.indirectly_referenced
        )
        registry = er.async_get(hass)

        # Get all entities in this domain
        all_entities = [
            e.entity_id for e in registry.entities.values() if e.domain == domain
        ]

        # Filter out excluded entities
        target_entities = [eid for eid in all_entities if eid not in excluded]

        if target_entities:
            # Each service call has different data included, we want to preserve
            # this and only change the target entities since we are using the
            # target entities as a blacklist.
            # This includes removing any areas, labels, or devices.
            service_data = dict(call.data)
            if "label_id" in service_data:
                service_data.pop("label_id")
            if "area_id" in service_data:
                service_data.pop("area_id")
            if "device_id" in service_data:
                service_data.pop("device_id")
            service_data["entity_id"] = target_entities

            # Send the modified service call to the appropriate domain.
            await hass.services.async_call(domain, action, service_data, blocking=True)

    # FANS
    async def turn_on_fans(call: ServiceCall):
        await _handle_domain_entities(call, "turn_on", "fan")

    async def turn_off_fans(call: ServiceCall):
        await _handle_domain_entities(call, "turn_off", "fan")

    async def toggle_fans(call: ServiceCall):
        await _handle_domain_entities(call, "toggle", "fan")

    async def set_direction_fans(call: ServiceCall):
        await _handle_domain_entities(call, "set_direction", "fan")

    async def increase_speed_fans(call: ServiceCall):
        await _handle_domain_entities(call, "increase_speed", "fan")

    async def decrease_speed_fans(call: ServiceCall):
        await _handle_domain_entities(call, "decrease_speed", "fan")

    # Register fan services
    hass.services.async_register(DOMAIN, "turn_on_fans", turn_on_fans)
    hass.services.async_register(DOMAIN, "turn_off_fans", turn_off_fans)
    hass.services.async_register(DOMAIN, "toggle_fans", toggle_fans)
    hass.services.async_register(DOMAIN, "set_direction_fans", set_direction_fans)
    hass.services.async_register(DOMAIN, "increase_speed_fans", increase_speed_fans)
    hass.services.async_register(DOMAIN, "decrease_speed_fans", decrease_speed_fans)

    # LIGHTS
    async def turn_on_lights(call: ServiceCall):
        await _handle_domain_entities(call, "turn_on", "light")

    async def turn_off_lights(call: ServiceCall):
        await _handle_domain_entities(call, "turn_off", "light")

    async def toggle_lights(call: ServiceCall):
        await _handle_domain_entities(call, "toggle", "light")

    async def set_brightness_lights(call: ServiceCall):
        await _handle_domain_entities(call, "set_brightness", "light")

    async def set_color_lights(call: ServiceCall):
        await _handle_domain_entities(call, "set_color", "light")

    # Register light services
    hass.services.async_register(DOMAIN, "turn_on_lights", turn_on_lights)
    hass.services.async_register(DOMAIN, "turn_off_lights", turn_off_lights)
    hass.services.async_register(DOMAIN, "toggle_lights", toggle_lights)
    hass.services.async_register(DOMAIN, "set_brightness_lights", set_brightness_lights)
    hass.services.async_register(DOMAIN, "set_color_lights", set_color_lights)

    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload Excluded integration."""
    return True