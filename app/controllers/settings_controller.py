from bottle import mako_template as template

from app.controllers.application_controller import ApplicationController


class SettingsController(ApplicationController):
    """Class for handling the settings page."""

    def index(self):
        """Render /settings page."""
        return template('settings/index.tpl')
