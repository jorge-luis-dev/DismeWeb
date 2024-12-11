from odoo import http
from odoo.addons.website.controllers.main import Home


class Main(Home):

    @http.route("/", auth="public", website=True)
    def index(self, **kwargs):
        super(Main, self).index(**kwargs)
        return 'Hello World!'
