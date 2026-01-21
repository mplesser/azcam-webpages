"""
DASH web server for azcam
"""

import logging

from dash import Dash, html, dcc, callback, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import dash_daq as daq
from fastapi.middleware.wsgi import WSGIMiddleware

import azcam
from azcam_webpages.status.status_card import statusweb_card


class StatusWeb(object):
    """
    Web server using Dash (plotly).
    """

    def __init__(self) -> None:

        azcam.db.statusweb = self

        self.app = Dash(
            __name__,
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            suppress_callback_exceptions=False,
            requests_pathname_prefix="/status/",
        )
        logging.getLogger("werkzeug").setLevel(logging.CRITICAL)  # stop messages

        self.statusweb_card = statusweb_card()

        # app layout
        self.app.layout = html.Div(
            [
                self.statusweb_card,
                dcc.Interval("statusweb_interval", interval=1_000, n_intervals=0),
            ]
        )

        azcam.db.webserver.app.mount("/status", WSGIMiddleware(self.app.server))

        self.logcommands = 1
        self.logstatus = 0

        return

    def set_message(self, message: str = "") -> None:
        """
        Set the browser message.
        """

        azcam.db.tools["exposure"].message = repr(message)
        return
