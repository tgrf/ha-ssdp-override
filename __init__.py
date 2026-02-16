"""Disabled SSDP integration to prevent routing table pollution."""
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType
import logging

_LOGGER = logging.getLogger(__name__)
DOMAIN = "ssdp"

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up SSDP integration (disabled)."""
    _LOGGER.warning("SSDP integration disabled by custom_components override")
    return True

async def async_setup_entry(hass, entry):
    """Set up from config entry (disabled)."""
    return True

async def async_unload_entry(hass, entry):
    """Unload config entry (disabled)."""
    return True
