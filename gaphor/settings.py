"""Application settings support for Gaphor."""

from gi.repository import Gio
import logging

APPLICATION_ID = "org.gaphor.Gaphor"

logger = logging.getLogger(__name__)


class Settings(Gio.Settings):
    """Gaphor settings."""

    @classmethod
    def new(cls) -> Gio.Settings | None:
        """Create a new Settings object."""
        schema_source = Gio.SettingsSchemaSource.get_default()
        if Gio.SettingsSchemaSource.lookup(schema_source, APPLICATION_ID, False):
            gio_settings = Gio.Settings.new(APPLICATION_ID)
            gio_settings.__class__ = Settings
            return gio_settings
        logger.info(
            "Settings schema not found and settings won't be saved, run `poe install-schemas`"
        )
        return None


settings = Settings.new()
